//-----------------------------------------------------------------------------
IOdictionary rigidMotionProperties
    (
        IOobject
        (
            "rigidMotionProperties",
            runTime.constant(),
            mesh,
            IOobject::MUST_READ,
            IOobject::NO_WRITE
        )
    );
word rigidMotionMode( rigidMotionProperties.lookup("rigidMotionMode") );

scalar omega ( readScalar( rigidMotionProperties.lookup("omega")  ) );
scalar degAm ( readScalar( rigidMotionProperties.lookup("degAm")  ) );
scalar magAcc( readScalar( rigidMotionProperties.lookup("magAcc") ) );

vector rotOrigin( rigidMotionProperties.lookup("rotOrigin") );

scalar pi        = 3.1415926535898;
scalar angAm     = pi*degAm/180;
//-----------------------------------------------------------------------------


