if (outerCorr ==1)
{
#          include "fsiAlgFixedPoint.H"       
}
else
{
    if (couplingScheme == "FixedRelaxation")
    {
#          include "fsiAlgFixedPoint.H"      
    }

    else if (couplingScheme == "Aitken")
    {   
#          include "readAitken.H"
#          include "fsiAlgAitken.H"
    }

    else if (couplingScheme == "IQN-ILS")
    { 
#          include "readIQN_ILS.H"
#          include "fsiAlgIQN_ILS.H"     
    }
    
    else if (couplingScheme == "IQN-ILSVarRelaxing")
    { 
#          include "readIQN_ILSVarRelaxing.H"
#          include "fsiAlgIQN_ILSVarRelaxing.H"     
    }

    else if (couplingScheme == "Mix-Aitken-IQN")
    {
#          include "readMix_Aitken_IQN.H"  
#          include "fsiAlgMix_Aitken_IQN.H"  
    }
    else
    {
        FatalErrorIn
        (
            "readFsiProperties"
        )   << "couplingScheme: " << couplingScheme
            << " is not a valid choice. "
            << "Options are: FixedRelaxation, Aitken, IQN-ILS, IQN-ILSVarRelaxing, Mix-Aitken-IQN"
            << abort(FatalError);
    }


     
}
