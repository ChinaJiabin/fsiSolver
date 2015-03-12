if(mesh.moving())
{
    // Make the fluxes relative
    phi -= fvc::meshPhi(U);
} 

#       include "CourantNo.H"

        fvVectorMatrix UEqn
        (
            fvm::ddt(U)
          + fvm::div(phi, U)
          - fvm::laplacian(nu, U)
        );

        if (pressureDrive)
        {
          if (outerCorr == 1)
            //如果流动以压力驱动为主，则动量修正只在每次时间的子迭代开始时进行一次
            {
             solve(UEqn == -fvc::grad(p));
            }
        }
        else
        {
             solve(UEqn == -fvc::grad(p));
        }

        // --- PISO loop
        volScalarField rUA = 1.0/UEqn.A();

        for (int corr=0; corr<nCorr; corr++)
        {   
            U = rUA*UEqn.H();
            phi = (fvc::interpolate(U) & mesh.Sf());
            adjustPhi(phi, U, p);
             
            for (int nonOrth=0; nonOrth<=nNonOrthCorr; nonOrth++)
            {
                fvScalarMatrix pEqn
                (
                    fvm::laplacian(rUA, p)
                 == fvc::div(phi)
                );

                pEqn.setReference(pRefCell, pRefValue);
                pEqn.solve();

                if (nonOrth == nNonOrthCorr)
                {
                    phi -= pEqn.flux();
                }
            }

#           include "continuityErrs.H"

            //---------------------------------------------
            //Add1:
            //Make the fluxes relative to the mesh motion
              if(mesh.moving())
             {
               phi -= fvc::meshPhi(U);
             }
            //----------------------------------------------

            U -= rUA*fvc::grad(p);
            U.correctBoundaryConditions();
        }
 
           //---------------------------------------------
           //Add2:
           //Make the fluxes absolute to the mesh motion
              if(mesh.moving())
             {
               phi += fvc::meshPhi(U);
             }
           //----------------------------------------------

       //Add:Solve energy equation
       /*
        solve
        (
            fvm::ddt(T)
          + fvm::div(phi, T)
          - fvm::laplacian(DT, T)
        );*/



