dictionary fsiSolution = couplingProperties.subDict("Mix-Aitken-IQN");
scalar maxRelaxFactor(readScalar( fsiSolution.lookup("maxRelaxFactor") ) );
int numSubStepsForAitken( readInt( fsiSolution.lookup("numSubStepsForAitken") ) );
int dim( readInt( fsiSolution.lookup("dim") ) );
int maxColumn( readInt( fsiSolution.lookup("maxColumn") ) );
