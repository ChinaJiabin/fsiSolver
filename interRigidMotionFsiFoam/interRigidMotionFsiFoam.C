#include "fvCFD.H"
#include "dynamicFvMesh.H"
#include "RBFMotionSolver.H"

#include "MULES.H"
#include "subCycle.H"
#include "interfaceProperties.H"
#include "twoPhaseMixture.H"
#include "turbulenceModel.H"

#include "constitutiveModel.H"
#include "solidTractionFvPatchVectorField.H"
#include "volPointInterpolation.H"
#include "pointPatchInterpolation.H"

#include "patchToPatchInterpolation.H"
#include "movingWallVelocityFvPatchVectorField.H"

#include "tetFemMatrices.H"
#include "tetPointFields.H"
#include "faceTetPolyPatch.H"
#include "tetPolyPatchInterpolation.H"
#include "fixedValueTetPolyPatchFields.H"
#include "fixedValuePointPatchFields.H"

#include "OFstream.H"
#include "IFstream.H"
#include "EulerDdtScheme.H"
#include "backwardDdtScheme.H"

#include "pointFields.H"
#include "fixedGradientFvPatchFields.H"
#include "primitivePatchInterpolation.H"
#include "twoDPointCorrector.H"
#include "scalarIOField.H"
#include "leastSquaresVolPointInterpolation.H"
#include "symmetryPolyPatch.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

int main(int argc, char *argv[])
{
#   include "setRootCase.H"
#   include "createTime.H"

#   include "createDynamicFvMesh.H"               
#   include "createFields.H"                            
#   include "createStressMesh.H"                        
#   include "createStressFields.H" 
                     
#   include "readCouplingProperties.H"
#   include "createZoneToZoneInterpolators.H"
#   include "initContinuityErrs.H"
#   include "findGlobalFaceZones.H"
#   include "CreateExtraplolationField.H" 

#   include "readPIMPLEControls.H"   
#   include "readTimeControls.H"
#   include "readRigidMotionControls.H"

#   include "correctPhi.H"
#   include "CourantNo.H"
#   include "setInitialDeltaT.H"   
//* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

    Info << "\nStarting time loop\n" << endl;

    for (runTime++; !runTime.end(); runTime++)
    {
        Info << "Time = " << runTime.timeName() << nl << endl;

#       include "createInterfaceFields.H"

        label outerCorr=0;
        do
        {
            outerCorr++;
    
#           include "moveFluidMesh.H"
#           include "solveFluid.H"

#           include "setInterfaceForce.H"
#           include "solveSolid.H"

#           include "calcFsiResidual.H"
#           include "fsiAlgorithm.H"

        }
        while
        (outerCorr < nOuterFsiCorr);

        Vs += DV;

#       include "setExtraplolationField.H"     
#       include "rotateSolidFields.H"
#       include "moveSolidMeshLeastSquares.H"
#       include "calculateStress.H"

        Info<< "ExecutionTime = " << runTime.elapsedCpuTime() << " s"
            << "  ClockTime = " << runTime.elapsedClockTime() << " s"
            << endl << endl;
    }

    Info<< "End\n" << endl;

    return(0);
}

// ************************************************************************* //
