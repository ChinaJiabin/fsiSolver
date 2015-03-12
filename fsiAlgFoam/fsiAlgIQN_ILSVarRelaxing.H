//--------------------------------------------------------------------------------------
// Parallel data exchange: collect fields on all processors
vectorField fsiZoneResidual
    (
	mesh.pointZones()[fsiPointsZoneID].size(), 
	vector::zero
    );

vectorField fsiZoneResidualOld
    (
	mesh.pointZones()[fsiPointsZoneID].size(), 
	vector::zero
    );

vectorField solidZonePointsDispl
    (
	mesh.pointZones()[fsiPointsZoneID].size(), 
	vector::zero
    );

vectorField solidZonePointsDisplOld
    (
	mesh.pointZones()[fsiPointsZoneID].size(), 
	vector::zero
    );

scalarField pointsOfNumShared
    (
	mesh.pointZones()[fsiPointsZoneID].size(), 
	0
    );    
const labelList& meshPoints = mesh.boundaryMesh()[fluidPatchID].meshPoints();
forAll(fsiResidual, pointI)
{   
    label pointId = mesh.pointZones()[0].whichPoint(meshPoints[pointI]);
    pointsOfNumShared[pointId] = 1.0;
    
    fsiZoneResidual[pointId] = fsiResidual[pointI]; 
    fsiZoneResidualOld[pointId] = fsiResidualOld[pointI]; 
    solidZonePointsDispl[pointId] = solidPatchPointsDispl[pointI];
    solidZonePointsDisplOld[pointId] = solidPatchPointsDisplOld[pointI];
}

reduce(fsiZoneResidual,         sumOp<vectorField>());
reduce(fsiZoneResidualOld,      sumOp<vectorField>());
reduce(solidZonePointsDispl,    sumOp<vectorField>());
reduce(solidZonePointsDisplOld, sumOp<vectorField>());
reduce(pointsOfNumShared, sumOp<scalarField>());

fsiZoneResidual/=pointsOfNumShared;
fsiZoneResidualOld/=pointsOfNumShared;
solidZonePointsDispl/=pointsOfNumShared;
solidZonePointsDisplOld/=pointsOfNumShared;
//--------------------------------------------------------------------------------------
int numDegreeOfFreedom( dim*mesh.pointZones()[fsiPointsZoneID].size() );
scalar rel(  min(maxRelaxFactor,startRelaxFactor*(outerCorr-1)  )  );
scalarRectangularMatrix vVector(numDegreeOfFreedom,1,0);
scalarRectangularMatrix temp(numDegreeOfFreedom,1,0);

if(Pstream::master())
{
  if(outerCorr > maxColumn+1)
  {
    deltaInput.removeHead();
    deltaOutput.removeHead();
  }

  scalarRectangularMatrix vMatrix(numDegreeOfFreedom,deltaInput.size()+1,0);
  scalarRectangularMatrix wMatrix(numDegreeOfFreedom,deltaInput.size()+1,0);

  //1.Assemble vMatrix  
  int numColumn(0);
  for(int id=0;id<numDegreeOfFreedom;id=id+dim)
      for(int i=0;i<dim;i++)
	  temp[id+i][0]=( fsiZoneResidualOld[id/dim][i]
	                 -fsiZoneResidual[id/dim][i]); 

  deltaInput.append(temp);

  forAllIter(SLList<scalarRectangularMatrix>,deltaInput,iter)
  { 
    for(int i=0;i<numDegreeOfFreedom;i++)    
	vMatrix[i][numColumn]=(*iter)[i][0];
    numColumn+=1;
  }

  //2.Assemble wMatrix 
  numColumn=0;
  for(int id=0;id<numDegreeOfFreedom;id=id+dim)
      for(int i=0;i<dim;i++)
	  temp[id+i][0]=( solidZonePointsDisplOld[id/dim][i]
	                 -solidZonePointsDispl[id/dim][i] );

  deltaOutput.append(temp);

  forAllIter(SLList<scalarRectangularMatrix>,deltaOutput,iter)
  {  
    for(int i=0;i<numDegreeOfFreedom;i++)    
	wMatrix[i][numColumn]=(*iter)[i][0];
    numColumn+=1;
  } 

  //3.Assemble vVecotr
  for(int id=0;id<numDegreeOfFreedom;id=id+dim)
      for(int i=0;i<dim;i++)
	  vVector[id+i][0]=-fsiZoneResidual[id/dim][i];
    
  //4.Calculate
  multiply(temp,wMatrix,SVDinv(vMatrix),vVector);
}
reduce(vVector, sumOp<scalarRectangularMatrix>());
reduce(temp,    sumOp<scalarRectangularMatrix>());

//5.Update fluidPatchPointsDispl
fluidPatchPointsDisplOld = fluidPatchPointsDispl;
forAll(fluidPatchPointsDispl,pointI)
{
  label pointId = mesh.pointZones()[0].whichPoint(meshPoints[pointI]);
  for(int i=0;i<dim;i++)
  {
   fluidPatchPointsDispl[pointI][i]+=rel*
   (temp[pointId*dim+i][0]-vVector[pointId*dim+i][0]);
  }
}
