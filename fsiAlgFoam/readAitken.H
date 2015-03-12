dictionary fsiSolution = couplingProperties.subDict("Aitken");
scalar maxRelaxFactor(readScalar( fsiSolution.lookup("maxRelaxFactor") ) );
