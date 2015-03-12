if (outerCorr ==1)
{      
   system(clearCommand);
}
   
{ 
  //-Write data
  OFstream writeFile0("fsi/prePoints");
  OFstream writeFile1("fsi/points");
  OFstream writeFile3("fsi/res");
  OFstream writeFile5("fsi/rel");

  forAll(solidPatchPointsDispl,id)
  {
  for(int i=0;i<dim;i++)
  writeFile0<<solidPatchPointsDispl[id][i]<<'\t';
  writeFile0<<'\n';
  }

  forAll(fluidPatchPointsDispl,id)
  {
  for(int i=0;i<dim;i++)
  writeFile1<<fluidPatchPointsDispl[id][i]<<'\t';
  writeFile1<<'\n';
  }

  forAll(fsiResidual,id)
  {
  for(int i=0;i<dim;i++)
  writeFile3<<fsiResidual[id][i]<<'\t';
  writeFile3<<'\n';
  }

  writeFile5<<fsiRelaxationFactor<<endl;   
}

//-------------------------------------
//For test
//-------------------------------------      
system(pythonCommand);
{ 
  //-Read data 
  double temp;
  IFstream readfile("fsi/newPoints");
  
  fluidPatchPointsDisplOld = fluidPatchPointsDispl;
  forAll(fluidPatchPointsDispl,id)
  {
    for(int i=0;i<dim;i++)
    {
      readfile.read(temp);
      fluidPatchPointsDispl[id][i]=temp;
    }
  }
  //-Read fsiRelaxationFactor
  IFstream readRel("fsi/rel");
  readRel.read(fsiRelaxationFactor);
}	






