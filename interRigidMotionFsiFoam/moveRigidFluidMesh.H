pointField newPoints = mesh.allPoints();
scalar curTime   = mesh.time().value();

if(rigidMotionMode == "rotation" )
{  
  //运动方式1：转动
  //-------------------------------------------------------------------------------------------------
  scalar deltaAng =  angAm*( Foam::sin( omega*(curTime + mesh.time().deltaT().value() ) ) 
			    -Foam::sin( omega*curTime ) );

  tensor rotZ
      (
	  Foam::cos(deltaAng), -Foam::sin(deltaAng), 0,
	  Foam::sin(deltaAng),  Foam::cos(deltaAng), 0,
	  0, 0, 1
      );

  mesh.movePoints( ( rotZ&(newPoints-rotOrigin) ) + rotOrigin );

  const labelList& meshPoints = mesh.boundaryMesh()[fluidPatchID].meshPoints();
  forAll(rigidPointsDispl, pointI)
  {
    rigidPointsDispl[pointI] =  ( rotZ & (newPoints[meshPoints[pointI]]-rotOrigin)  )
				-( newPoints[meshPoints[pointI]] - rotOrigin );
  }

  vectorField faceCentre = stressMesh.Cf().boundaryField()[1];
  forAll(faceCentre,pointI)
  {
    DU.boundaryField()[1][pointI] =  ( rotZ & (faceCentre[pointI] - rotOrigin) )
				    -( faceCentre[pointI] - rotOrigin );
  }
} 
else if(rigidMotionMode == "translation")
{
  //-------------------------------------------------------------------------------------------------
  //运动方式2:平动
  //S = A/\omega^2 (1 - sin(\omega t) )
  vector deltaDist(  magAcc*(
			    Foam::cos( omega*curTime )
			  -Foam::cos( omega*curTime+ mesh.time().deltaT().value() ) 
			  )/sqr(omega)
		     ,0,0
		  );
  mesh.movePoints( newPoints + deltaDist );

  rigidPointsDispl = deltaDist;

  forAll( DU.boundaryField()[1],faceI )
  {
    DU.boundaryField()[1][faceI] = deltaDist;
  }
  //-------------------------------------------------------------------------------------------------
}




