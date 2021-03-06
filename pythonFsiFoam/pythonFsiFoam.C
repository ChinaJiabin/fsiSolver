/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | foam-extend: Open Source CFD
   \\    /   O peration     |
    \\  /    A nd           | For copyright notice see file Copyright
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of foam-extend.

    foam-extend is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or (at your
    option) any later version.

    foam-extend is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with foam-extend.  If not, see <http://www.gnu.org/licenses/>.

Application
    icoFsiElastciNonLinSolidFoam

Description
    Transient solver for fluid-solid interaction for an incompressible
    fluid and a large strain solid
    solid mesh is moved using U interpolated using least squares method

Author
    Zeljko Tukovic FSB Zagreb
    adapted by Philip Cardiff
    adapted by Jiabin

\*---------------------------------------------------------------------------*/

#include "fvCFD.H"
#include "dynamicFvMesh.H"

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
#   include "createExtraplolationField.H"           //New add
//* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

    Info << "\nStarting time loop\n" << endl;
   
    for (runTime++; !runTime.end(); runTime++)
    {
        Info << "Time = " << runTime.timeName() << nl << endl;

#       include "readPISOControls.H"

#       include "readFsiControls.H"

#       include "createStressPointMesh.H"

#       include "createInterfaceFields.H"

        label outerCorr=0;

        //---------------------------------------------------------------
        //Info<<"X displacement:"<<stressMesh.points()[1391][0]-0.6<<endl;   
        //Info<<"Y displacement:"<<stressMesh.points()[1391][1]-0.2<<endl;   
        //---------------------------------------------------------------

        do
        {
            outerCorr++;

#           include "moveFluidMesh.H"
#           include "solveFluid.H"

#           include "setInterfaceForce.H"
#           include "solveSolid.H"

#           include "calcFsiResidual.H"
#           include "pythonFsiAlgorithm.H"
        }
        while
        ( outerCorr < nOuterCorr );
        Vs += DV;

#       include "setExtraplolationField.H"      //New add
#       include "rotateSolidFields.H"
#       include "moveSolidMeshLeastSquares.H"
#       include "calculateStress.H"
#       include "calculateLiftAndDrag.H"
        
        Info<< "ExecutionTime = " << runTime.elapsedCpuTime() << " s"
            << "  ClockTime = " << runTime.elapsedClockTime() << " s"
            << endl << endl;
    }

    Info<< "End\n" << endl;

    return(0);
}

// ************************************************************************* //
