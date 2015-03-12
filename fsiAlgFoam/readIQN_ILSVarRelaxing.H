dictionary fsiSolution = couplingProperties.subDict("IQN-ILSVarRelaxing");
int dim( readInt( fsiSolution.lookup("dim") ) );
int maxColumn( readInt( fsiSolution.lookup("maxColumn") ) );
scalar startRelaxFactor(readScalar( fsiSolution.lookup("startRelaxFactor") ) );
scalar maxRelaxFactor(readScalar( fsiSolution.lookup("maxRelaxFactor") ) );
