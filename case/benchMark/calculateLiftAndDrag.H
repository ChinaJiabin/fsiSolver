const dictionary& statistics = mesh.solutionDict().subDict("statistics");
bool calculateLiftAndDrag = false;
if (statistics.found("calculateLiftAndDrag"))
   {
      calculateLiftAndDrag = Switch(statistics.lookup("calculateLiftAndDrag"));
   }

if (calculateLiftAndDrag)
{
//- calculate lift and drag for plate and cylinder due to pressure (ignore shear stress)
label plateID = mesh.boundaryMesh().findPatchID("plate");
label cylinderID = mesh.boundaryMesh().findPatchID("cylinder");

if(plateID == -1 || cylinderID == -1)
  {
    FatalError << "\n Cannot find the plate patch or the cylinder"
	       << " patch to calculate lift and drag!"
	       << exit(FatalError);
  }

scalar lift = 0;
scalar drag = 0;

 const vectorField& Sfp = mesh.boundary()[plateID].Sf();
 const scalarField& faceForceP = p.boundaryField()[plateID];
 const vectorField& faceForceT = -nu.value()*U.boundaryField()[plateID].snGrad();

forAll(p.boundaryField()[plateID], facei)
{
  lift += vector(0,1,0) & ( faceForceP[facei] * Sfp[facei] + faceForceT[facei]*mag(Sfp[facei])  );
  drag += vector(1,0,0) & ( faceForceP[facei] * Sfp[facei] + faceForceT[facei]*mag(Sfp[facei]) );
}

 const vectorField& Sfc = mesh.boundary()[cylinderID].Sf();
 const scalarField& faceForcePc = p.boundaryField()[cylinderID];
 const vectorField& faceForceTc = -nu.value()*U.boundaryField()[cylinderID].snGrad();

forAll(p.boundaryField()[cylinderID], facei)
{
  lift += vector(0,1,0) & ( faceForcePc[facei] * Sfc[facei] + faceForceTc[facei]*mag(Sfp[facei]) );
  drag += vector(1,0,0) & (faceForcePc[facei] * Sfc[facei] +  faceForceTc[facei]*mag(Sfp[facei]) );
}

 scalar width = 0.050668;

Info << "Total lift on the cylinder and plate boundaries is " << lift << " N, per unit width is " << (lift/width) << " N\n"
     << "Total drag on the cylinder and plate boundaries is " << drag << " N, per unit width is " << (drag/width) << " N\n"
     << endl;
}
