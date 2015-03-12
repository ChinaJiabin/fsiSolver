timeIterNum+=1;
vectorField fluidPatchPointsDispl
(
     mesh.boundaryMesh()[fluidPatchID].nPoints(),
     vector::zero
 );

if( timeIterNum == 3)
{
    fluidPatchPointsDispl = (2*fluidPatchPointsDisplOldTime1-fluidPatchPointsDisplOldTime2);
}
if (timeIterNum>3)
{
    fluidPatchPointsDispl = (2.5*fluidPatchPointsDisplOldTime1-2*fluidPatchPointsDisplOldTime2+0.5*fluidPatchPointsDisplOldTime3);
}

vectorField fluidPatchPointsDisplOld
(
     mesh.boundaryMesh()[fluidPatchID].nPoints(),
     vector::zero
);


vectorField solidPatchPointsDispl
(
    mesh.boundaryMesh()[fluidPatchID].nPoints(),
    vector::zero
);

vectorField solidPatchPointsDisplOld
(
    mesh.boundaryMesh()[fluidPatchID].nPoints(),
    vector::zero
);

vectorField fsiResidual
(
    mesh.boundaryMesh()[fluidPatchID].nPoints(),
    vector::zero
);

vectorField fsiResidualOld
(
    mesh.boundaryMesh()[fluidPatchID].nPoints(),
    vector::zero
);

vectorField solidPatchTraction
(
    stressMesh.boundary()[solidPatchID].size(), 
    vector::zero
);

scalarField solidPatchPressure
(
    stressMesh.boundary()[solidPatchID].size(), 
    0.0
);

vectorField rigidPointsDispl
(
    mesh.boundaryMesh()[fluidPatchID].nPoints(),
    vector::zero
);

scalar initialFsiResidualNorm = 0;
scalar fsiResidualNorm = 0;

SLList<scalarRectangularMatrix> deltaInput;
SLList<scalarRectangularMatrix> deltaOutput;


