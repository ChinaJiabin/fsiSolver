//--------------------------------------------------------------------------------------
// Parallel data exchange: collect fields on all processors
vectorField solidZonePointsDispl
    (
	mesh.pointZones()[0].size(), 
	vector::zero
    );

vectorField fluidZonePointsDispl
    (
	mesh.pointZones()[0].size(), 
	vector::zero
    );

vectorField fsiZoneResidual
    (
	mesh.pointZones()[0].size(), 
	vector::zero
    );

vectorField pointDisplField
    (
	mesh.pointZones()[0].size(), 
	vector::zero
    );

scalarField pointsOfNumShared
    (
	mesh.pointZones()[0].size(), 
	0
    );     
const labelList& meshPoints = mesh.boundaryMesh()[fluidPatchID].meshPoints();
forAll(solidPatchPointsDispl, pointI)
{
  label pointId = mesh.pointZones()[0].whichPoint(meshPoints[pointI]);
  pointsOfNumShared[pointId] = 1.0;
  
  solidZonePointsDispl[pointId] = solidPatchPointsDispl[pointI];  
  fluidZonePointsDispl[pointId] = fluidPatchPointsDispl[pointI];  
  fsiZoneResidual[pointId]      = fsiResidual[pointI]; 
}

reduce(solidZonePointsDispl, sumOp<vectorField>());
reduce(fluidZonePointsDispl, sumOp<vectorField>());
reduce(fsiZoneResidual,      sumOp<vectorField>());

reduce(pointsOfNumShared,    sumOp<scalarField>());
solidZonePointsDispl/=pointsOfNumShared;
fluidZonePointsDispl/=pointsOfNumShared;
fsiZoneResidual/=pointsOfNumShared;
//--------------------------------------------------------------------------------------
if(Pstream::master())
{
  if (outerCorr ==1)
  {     
      system(clearCommand);
  }

  //1:Write data  
  { 
    OFstream writeFile0("fsi/prePoints");
    OFstream writeFile1("fsi/points");
    OFstream writeFile2("fsi/res");
    OFstream writeFile3("fsi/rel");

    forAll(solidZonePointsDispl,id)
    {
    for(int i=0;i<dim;i++)
    writeFile0<<solidZonePointsDispl[id][i]<<'\t';
    writeFile0<<'\n';
    }

    forAll(fluidZonePointsDispl,id)
    {
    for(int i=0;i<dim;i++)
    writeFile1<<fluidZonePointsDispl[id][i]<<'\t';
    writeFile1<<'\n';
    }

    forAll(fsiZoneResidual,id)
    {
    for(int i=0;i<dim;i++)
    writeFile2<<fsiResidual[id][i]<<'\t';
    writeFile2<<'\n';
    }

    writeFile3<<fsiRelaxationFactor<<endl;   
  }
  //2:Fsi algorithm 
  system(pythonCommand); 

  //3:Read data 
  { 
    double pointDispl;
    IFstream readfile("fsi/newPoints");
  
    forAll(pointDisplField,id)
    {
      for(int i=0;i<dim;i++)
      {
	readfile.read(pointDispl);
	pointDisplField[id][i]=pointDispl;
      }
    }
    //-Read fsiRelaxationFactor
    IFstream readRel("fsi/rel");
    readRel.read(fsiRelaxationFactor);
  }	
}
//Update fluidPatchPointsDispl
reduce(pointDisplField,    sumOp<vectorField>());
reduce(fsiRelaxationFactor,sumOp<scalar>());

fluidPatchPointsDisplOld = fluidPatchPointsDispl;
forAll(fluidPatchPointsDispl,pointI)
{
  label pointId = mesh.pointZones()[0].whichPoint(meshPoints[pointI]);
  fluidPatchPointsDispl[pointI]= pointDisplField[pointId];
}
