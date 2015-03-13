//For extraplolation of the interface position based on the previous time step
    vectorField fluidPatchPointsDisplOldTime1
    (
     mesh.boundaryMesh()[fluidPatchID].nPoints(),
     vector::zero
    );

    vectorField fluidPatchPointsDisplOldTime2
    (
     mesh.boundaryMesh()[fluidPatchID].nPoints(),
     vector::zero
    );

    vectorField fluidPatchPointsDisplOldTime3
    (
     mesh.boundaryMesh()[fluidPatchID].nPoints(),
     vector::zero
    );

int timeIterNum = 0;
//
