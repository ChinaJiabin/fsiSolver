dictionary fsiSolution = couplingProperties.subDict("IQN-ILS");
int dim( readInt( fsiSolution.lookup("dim") ) );
int maxColumn( readInt( fsiSolution.lookup("maxColumn") ) );

