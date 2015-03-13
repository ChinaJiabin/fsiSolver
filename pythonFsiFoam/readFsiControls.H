word couplingScheme;

if (couplingProperties.found("couplingScheme"))
{
    couplingScheme = word(couplingProperties.lookup("couplingScheme"));

    if 
    (
        (couplingScheme == "IQN-ILS") 
     || (couplingScheme == "Aitken")
     || (couplingScheme == "FixedRelaxation")
    )
    {
        Info<< "Selecting coupling scheme " << couplingScheme << endl;
    }
    else
    {
        FatalErrorIn
        (
            "readFsiProperties"
        )   << "couplingScheme: " << couplingScheme
            << " is not a valid choice. "
            << "Options are: IQN-ILS, Aitken, FixedRelaxation"
            << abort(FatalError);
    }
}

scalar interfaceDeformationLimit
(
    readScalar(couplingProperties.lookup("interfaceDeformationLimit"))
);


IOdictionary dynamicMeshDict
(
    IOobject
    (
        "dynamicMeshDict",
        runTime.constant(),
        mesh,
        IOobject::MUST_READ,
        IOobject::NO_WRITE,
        false
    )
);

scalar fsiRelaxationFactor;
fsiRelaxationFactor = scalar
(
    readScalar(couplingProperties.lookup("fsiRelaxationFactor"))
);


scalar outerCorrTolerance
(
    readScalar(couplingProperties.lookup("outerCorrTolerance"))
); 

Switch fsi(couplingProperties.lookup("fsi"));
//------------------------------------------------------
//Add
dictionary fsiSolution = mesh.solutionDict().subDict("fsi");

word pythonCommand( fsiSolution.lookup("pythonCommand"),false );
word clearCommand( fsiSolution.lookup("clearCommand"),false );

int dim( readInt( fsiSolution.lookup("dim") ) );
//-------------------------------------------------------

