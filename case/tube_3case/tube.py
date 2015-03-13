#lanMesh
#A parametric hexahedral mesh generator 
import os
import sys
sys.path.append("/home/jiabin/python/lan/")
import lanMesh
import numpy as np
#------------------------------------------------------------------------------------------------
#convertToMeters
convert=1

#geometeryParameter:
tubeInnerRadius = 0.005
tubeLength = 0.05
tubeThickness = 0.001
ogridRadius = 0.0025
ogridSplitRatio = 0.6

#patches
patchName=['inlet','outlet','fsiface']
patchType=['wall']*len(patchName)

patchName_solid=['inlet','outlet','wall','fsiface']
patchType_solid=['wall']*len(patchName_solid)

#meshNumber
unitLen = 0.0003
meshNum_arc = int(0.5*np.pi*tubeInnerRadius/unitLen)
meshNum_r   = int(tubeInnerRadius*(1-ogridSplitRatio)/unitLen)+5
meshNum_z   = int(tubeLength/unitLen)
meshNum_t   = int(tubeThickness/unitLen*2)

#meshGrad
meshGrad_arc = 1
meshGrad_r   = 1
meshGrad_z   = 1
meshGrad_t   = 1

#edge
edgeType = ['arc']*16
edgeType_solid = ['arc']*16

#path
file_read_path="/home/jiabin/python/lan/blockMeshDict_model"
file_write_path="constant/polyMesh/blockMeshDict"
file_write_path_solid="constant/solid/polyMesh/blockMeshDict"
#------------------------------------------------------------------------------------------------
#Fluid
points=np.array([[ 0.5*tubeInnerRadius*np.sqrt(2),  0.5*tubeInnerRadius*np.sqrt(2),0],                                     #-0
                 [-0.5*tubeInnerRadius*np.sqrt(2),  0.5*tubeInnerRadius*np.sqrt(2),0],
                 [-0.5*tubeInnerRadius*np.sqrt(2), -0.5*tubeInnerRadius*np.sqrt(2),0],
                 [ 0.5*tubeInnerRadius*np.sqrt(2), -0.5*tubeInnerRadius*np.sqrt(2),0]])
points=lanMesh.add(points,ogridSplitRatio,'*') 
points=lanMesh.add(points,tubeLength,'[:,2]+')
#-------------------------------------------------------------------------------
blocks = np.array([[5,4,0,1],[2,6,5,1],[2,3,7,6],[7,3,0,4],[6,7,4,5]])
blocks=lanMesh.add(blocks,8,'+','h')
#-------------------------------------------------------------------------------
meshNum = [[meshNum_arc,meshNum_r,  meshNum_z],
           [meshNum_r,  meshNum_arc,meshNum_z],
           [meshNum_arc,meshNum_r,  meshNum_z],
           [meshNum_r,  meshNum_arc,meshNum_z],
           [meshNum_arc,meshNum_arc,meshNum_z]]
           
meshGrad = [[meshGrad_arc,1.0/meshGrad_r,  meshGrad_z],
            [meshGrad_r,  meshGrad_arc,meshGrad_z],
            [meshGrad_arc,meshGrad_r,  meshGrad_z],
            [1.0/meshGrad_r,  meshGrad_arc,meshGrad_z],
            [meshGrad_arc,meshGrad_arc,meshGrad_z]]
#-------------------------------------------------------------------------------
edgePointId =np.array([[0,1],[1,2],[2,3],[3,0]])

for i in range(2):
  edgePointId=lanMesh.add(edgePointId,4*(i+1),'+')
  
edgePoint =np.array([[[0,tubeInnerRadius,0]   ],
                     [[-tubeInnerRadius,0,0]  ],
                     [[0,-tubeInnerRadius,0]  ],
                     [[tubeInnerRadius,0,0]   ],
                     [[0,ogridRadius,0]       ],   #
                     [[-ogridRadius,0,0]      ],
                     [[0,-ogridRadius,0]      ],
                     [[ogridRadius,0,0]       ]])
                     
edgePoint=lanMesh.add(edgePoint,tubeLength,'[:,:,2]+')
#-------------------------------------------------------------------------------
#
patches=[ [ [0,2],[1,2],[2,2],[3,2],[4,2] ],     #inlet
          [ [0,1],[1,1],[2,1],[3,1],[4,1] ],     #outlet 
          [ [0,5],[1,3],[2,6],[3,4]       ]]     #fsiface
#------------------------------------------------------------------------------------------------
#Solid
tubeOuterRadius = (tubeInnerRadius + tubeThickness);
points_solid=np.array([[ 0.5*tubeOuterRadius*np.sqrt(2),  0.5*tubeOuterRadius*np.sqrt(2),0],                                     #-0
                       [-0.5*tubeOuterRadius*np.sqrt(2),  0.5*tubeOuterRadius*np.sqrt(2),0],
                       [-0.5*tubeOuterRadius*np.sqrt(2), -0.5*tubeOuterRadius*np.sqrt(2),0],
                       [ 0.5*tubeOuterRadius*np.sqrt(2), -0.5*tubeOuterRadius*np.sqrt(2),0]])

points_solid=lanMesh.add(points_solid,(tubeInnerRadius/tubeOuterRadius),'*') 
points_solid=lanMesh.add(points_solid,tubeLength,'[:,2]+')

blocks_solid=blocks[0:4]

meshNum_solid =[[meshNum_arc,meshNum_t,  meshNum_z],
		 [meshNum_t,  meshNum_arc,meshNum_z],
		 [meshNum_arc,meshNum_t,  meshNum_z],
		 [meshNum_t,  meshNum_arc,meshNum_z]]
           
meshGrad_solid = [[meshGrad_arc,meshGrad_t,  meshGrad_z],
                  [meshGrad_t,  meshGrad_arc,meshGrad_z],
                  [meshGrad_arc,meshGrad_t,  meshGrad_z],
                  [meshGrad_t,  meshGrad_arc,meshGrad_z]]
                  
edgePointId_solid = edgePointId;

edgePoint_solid =np.array([[[0,tubeOuterRadius,0]  ],   #
                          [[-tubeOuterRadius,0,0]  ],
                          [[0,-tubeOuterRadius,0]  ],
                          [[tubeOuterRadius,0,0]   ],
                          [[0,tubeInnerRadius,0]   ],
                          [[-tubeInnerRadius,0,0]  ],
                          [[0,-tubeInnerRadius,0]  ],
                          [[tubeInnerRadius,0,0]   ]])
                 
edgePoint_solid=lanMesh.add(edgePoint_solid,tubeLength,'[:,:,2]+')


patches_solid= [ [ [0,2],[1,2],[2,2],[3,2] ],     #inlet
                 [ [0,1],[1,1],[2,1],[3,1] ],     #outlet 
                 [ [0,5],[1,3],[2,6],[3,4] ],     #wall
                 [ [0,6],[1,4],[2,5],[3,3] ]]     #fsiface                
#------------------------------------------------------------------------------------------------

os.system('rm -rf constant/polyMesh/*')
lanMesh.writeBlockMeshDict(file_read_path,file_write_path,
                              convert,points,blocks,meshNum,meshGrad,  
                              patchType,patchName,patches,
                              edgeType,edgePoint,edgePointId)
os.system('blockMesh')
os.system('foamToVTK')

os.system('setSet -batch batch.setSet')
os.system('setsToZones -noFlipMap')


os.system('rm -rf constant/solid/polyMesh/*')
lanMesh.writeBlockMeshDict(file_read_path,file_write_path_solid,
                              convert,points_solid,blocks_solid,meshNum_solid,meshGrad_solid,
                              patchType_solid,patchName_solid,patches_solid,
                              edgeType_solid,edgePoint_solid,edgePointId_solid)
                                                        
os.system('blockMesh -region solid')
os.system('foamToVTK -region solid')

os.system('setSet -region solid -batch batch.setSet')
os.system('setsToZones -region solid -noFlipMap')

#------------------------------------------------------------------------------------------------    
