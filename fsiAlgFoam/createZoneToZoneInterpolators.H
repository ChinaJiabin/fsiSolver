
zoneToZoneInterpolation* interpolatorFluidSolidPtr = NULL;
zoneToZoneInterpolation* interpolatorSolidFluidPtr = NULL;


if(!interpolatorFluidSolidPtr || !interpolatorSolidFluidPtr)
{
    deleteDemandDrivenData(interpolatorFluidSolidPtr);
    deleteDemandDrivenData(interpolatorSolidFluidPtr);

    Info << "Create fluid-to-solid and solid-to-fluid interpolators" << endl;

    interpolatorFluidSolidPtr = new zoneToZoneInterpolation
    (
        mesh.faceZones()[fluidZoneID](),
        stressMesh.faceZones()[solidZoneID](),
        intersection::VISIBLE
    );

    interpolatorSolidFluidPtr = new zoneToZoneInterpolation
    (
        stressMesh.faceZones()[solidZoneID](),
        mesh.faceZones()[fluidZoneID](),
        intersection::VISIBLE
    );
}

zoneToZoneInterpolation& interpolatorFluidSolid = 
    *interpolatorFluidSolidPtr;

zoneToZoneInterpolation& interpolatorSolidFluid = 
    *interpolatorSolidFluidPtr;

