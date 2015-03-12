   muEff = twoPhaseProperties.muf() + fvc::interpolate(rhoMix*turbulence->nut());

    fvVectorMatrix UEqn
    (
        fvm::ddt(rhoMix, U)
      + fvm::div(rhoPhi, U)
      - fvm::laplacian(muEff, U)
      - (fvc::grad(U) & fvc::grad(muEff))
    //- fvc::div(muEff*(fvc::interpolate(dev(fvc::grad(U))) & mesh.Sf()))
    );

    UEqn.relax();

    if (momentumPredictor)
    {
        solve
        (
            UEqn
         ==
            fvc::reconstruct
            (
                (
                    fvc::interpolate(interface.sigmaK())*fvc::snGrad(alpha1)
                  - ghf*fvc::snGrad(rhoMix)
                  - fvc::snGrad(pd)
                ) * mesh.magSf()
            )
        );
    }
