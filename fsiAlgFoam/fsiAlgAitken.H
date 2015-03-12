fsiRelaxationFactor = 
   -fsiRelaxationFactor
   *(
        gSum
        (
            fsiResidualOld
           &(fsiResidual - fsiResidualOld)
        )
       /(
            gSum
            (
                (fsiResidual - fsiResidualOld)
               &(fsiResidual - fsiResidualOld)
            )
        )
   );

fsiRelaxationFactor = sign(fsiRelaxationFactor)*min(maxRelaxFactor,mag(fsiRelaxationFactor));
  
Info << "Current fsi under-relaxation factor (Aitken): " 
    << fsiRelaxationFactor << endl;        

fluidPatchPointsDisplOld = fluidPatchPointsDispl;

fluidPatchPointsDispl += 
    fsiRelaxationFactor*fsiResidual;
