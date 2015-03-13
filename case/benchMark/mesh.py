import copy
import numpy as np
import os
import sys
sys.path.append("/home/jiabin/python/lan/")
import lanMesh
import numpy as np
#------------------------------------------------------------------------------------------------
Length = 2.5
Height = 0.41

circleCenter_x = 0.2
circleCenter_y = 0.2
circleRadius   = 0.05

beamLength     = 0.35
beamHeight     = 0.02

oGridRadius    = 2.5*circleRadius

unitLen = 0.0025

#meshGrad
meshGrad_x1         = 0.5
meshGrad_x3         = 2
meshGrad_x4         = 5
meshGrad_around     = 2.5

meshGrad_y1         = 0.8
meshGrad_y3         = 1.25

meshGrad_yBeam_up    = 1.3 
meshGrad_yBeam_down  = 1/1.3
#patches
patchName=['inlet','outlet','plate','cylinder','bottom','top']
patchType=['wall']*len(patchName)

patchName_solid=['plateFix','plate']
patchType_solid=['wall']*len(patchName_solid)
#------------------------------------------------------------------------------------------------
#convertToMeters
convert= 1

#geometeryParameter:
xLength_1 = circleCenter_x - oGridRadius*np.cos(np.pi/4)
xLength_2 = 2*circleCenter_x - xLength_1
xLength_3 = circleCenter_x + circleRadius + beamLength
xLength_4 = Length

xCircle_1 = circleCenter_x - circleRadius*np.cos(np.pi/4)  
xCircle_2 = circleCenter_x + circleRadius*np.cos(np.pi/4)  
xCircle_3 = circleCenter_x + np.sqrt(circleRadius**2-(beamHeight/2)**2)

yLength_1 = circleCenter_y-(circleCenter_x - xLength_1)
yLength_2 = 2*circleCenter_y - yLength_1
yLength_3 = Height

yCircle_1 = circleCenter_y - circleRadius*np.cos(np.pi/4)  
yCircle_2 = circleCenter_y + circleRadius*np.cos(np.pi/4)  

yBeam_1   = circleCenter_y - beamHeight/2
yBeam_2   = circleCenter_y + beamHeight/2

zLength   = 0.01

#meshNumber
meshNum_x1 = int(xLength_1/unitLen)
meshNum_x2 = int((xLength_2-xLength_1)/unitLen)+4
meshNum_x3 = int((xLength_3-xLength_2)/unitLen)+25
meshNum_x4 = int((xLength_4-xLength_3)/unitLen/2.2)

meshNum_y1 = int(yLength_1/unitLen)
meshNum_y2 = int((yLength_2-yLength_1)/unitLen)
meshNum_y3 = int((yLength_3-yLength_2)/unitLen)

meshNum_yBeam      = int(beamHeight/unitLen)+4
meshNum_yBeam_down = int((yBeam_1-yLength_1)/unitLen)+5
meshNum_yBeam_up   = int((yLength_2-yBeam_2)/unitLen)+5

meshNum_around = meshNum_x2

#path
file_read_path="/home/jiabin/python/lan/blockMeshDict_model"
file_write_path="constant/polyMesh/blockMeshDict"
file_write_path_solid="constant/solid/polyMesh/blockMeshDict"
#------------------------------------------------------------------------------------------------
points=np.array([ [ 0,        0,   0], 
                  [xLength_1, 0,   0],
                  [xLength_2, 0,   0],
                  [xLength_3, 0,   0],
                  [xLength_4, 0,   0] ])

pointsOther = np.array( [ [xCircle_1, yCircle_1, 0 ],
                          [xCircle_2, yCircle_1, 0 ],   
                          [xCircle_3, yBeam_1,   0 ], 
                          [circleCenter_x + 0.85*oGridRadius, yBeam_1,   0 ],
                          [xLength_3, yBeam_1,   0 ],
                          [xLength_4, yBeam_1,   0 ], #
                          [xCircle_1, yCircle_2, 0 ],
                          [xCircle_2, yCircle_2, 0 ],   
                          [xCircle_3, yBeam_2,   0 ], 
                          [circleCenter_x + 0.85*oGridRadius, yBeam_2,   0 ],
                          [xLength_3, yBeam_2,   0 ],
                          [xLength_4, yBeam_2,   0 ] ] )

points = lanMesh.addContinue(points,[yLength_1,yLength_2,yLength_3],'[:,1]')
points = np.vstack((points,pointsOther))
points = lanMesh.add(points,zLength,'[:,2]+') 
#------------------------------------------------------------------------------------------------
blocks = np.array([ [0,1,6,5],
                    [1,2,7,6],
                    [2,3,8,7],
                    [3,4,9,8],     #
                    [5,6,11,10],
                    [6,7,21,20],
                    [7,8,24,23],
                    [8,9,25,24],   #
                    [6,20,26,11],
                    [21,7,23,22],
                    [24,25,31,30], # 
                    [26,27,12,11],
                    [28,29,12,27],
                    [29,30,13,12],
                    [30,31,14,13], #
                    [10,11,16,15],
                    [11,12,17,16],
                    [12,13,18,17],
                    [13,14,19,18]])
blocks = lanMesh.add(blocks,len(points)/2,'+','h')
#--------------------------------
#For test
#meshNum = [[20,20,1]]*len(blocks)
#--------------------------------

#-------------------------------------------------------------------------------

meshNum = [[meshNum_x1, meshNum_y1, 1             ],
           [meshNum_x2, meshNum_y1, 1             ],
           [meshNum_x3, meshNum_y1, 1             ],
           [meshNum_x4, meshNum_y1, 1             ],          ########4
           [meshNum_x1, meshNum_y2, 1             ],
           [meshNum_x2, meshNum_around, 1         ],
           [meshNum_x3, meshNum_yBeam_down, 1     ],
           [meshNum_x4, meshNum_yBeam_down, 1     ],          ########8 
           [meshNum_around,meshNum_y2, 1          ], 
           [meshNum_around,meshNum_yBeam_down, 1  ],
           [meshNum_x4, meshNum_yBeam,1           ],          ########11
           [meshNum_x2, meshNum_around, 1         ],
           [meshNum_around,meshNum_yBeam_up, 1    ],
           [meshNum_x3, meshNum_yBeam_up, 1       ],
           [meshNum_x4, meshNum_yBeam_up, 1       ],          ########15
           [meshNum_x1, meshNum_y3, 1             ],
           [meshNum_x2, meshNum_y3, 1             ],
           [meshNum_x3, meshNum_y3, 1             ],
           [meshNum_x4, meshNum_y3, 1             ] ]  

meshGrad = np.ones([len(blocks),3])   

meshGrad[5][1]   = 1.0/meshGrad_around 
meshGrad[11][1]  = meshGrad_around 
meshGrad[9][0]   = meshGrad_around 
meshGrad[12][0]  = meshGrad_around
meshGrad[8][0]   = 1.0/meshGrad_around

meshGrad[0][0]   = meshGrad_x1
meshGrad[4][0]   = meshGrad_x1
meshGrad[15][0]  = meshGrad_x1

meshGrad[2][0]   = meshGrad_x3
meshGrad[6][0]   = meshGrad_x3
meshGrad[13][0]  = meshGrad_x3
meshGrad[17][0]  = meshGrad_x3

meshGrad[3][0]   = meshGrad_x4
meshGrad[7][0]   = meshGrad_x4
meshGrad[10][0]  = meshGrad_x4
meshGrad[14][0]  = meshGrad_x4
meshGrad[18][0]  = meshGrad_x4

meshGrad[0][1]   = meshGrad_y1
meshGrad[1][1]   = meshGrad_y1
meshGrad[2][1]   = meshGrad_y1
meshGrad[3][1]   = meshGrad_y1

meshGrad[15][1]   = meshGrad_y3
meshGrad[16][1]   = meshGrad_y3
meshGrad[17][1]   = meshGrad_y3
meshGrad[18][1]   = meshGrad_y3

meshGrad[12][1]   = meshGrad_yBeam_up
meshGrad[13][1]   = meshGrad_yBeam_up
meshGrad[14][1]   = meshGrad_yBeam_up

meshGrad[9][1]   = meshGrad_yBeam_down
meshGrad[6][1]   = meshGrad_yBeam_down
meshGrad[7][1]   = meshGrad_yBeam_down
#-------------------------------------------------------------------------------
edgePointId =np.array([ [20,21],[21,22],[28,27],[27,26],[26,20],[6,7],[7,23],[29,12],[12,11],[11,6] ])
edgePointId =lanMesh.add(edgePointId,len(points)/2,'+')
  
edgePoint =np.array([ [ [circleCenter_x                                     ,circleCenter_y-circleRadius                      , 0     ]  ],
                      [ [circleCenter_x + circleRadius*np.cos(np.pi/8)      ,circleCenter_y-circleRadius*np.sin(np.pi/8)      , 0     ]  ],
                      [ [circleCenter_x + circleRadius*np.cos(np.pi/8)      ,circleCenter_y+circleRadius*np.sin(np.pi/8)      , 0     ]  ],
                      [ [circleCenter_x                                     ,circleCenter_y+circleRadius                      , 0     ]  ],
                      [ [circleCenter_x-circleRadius                        ,circleCenter_y                                   , 0     ]  ],  ###
                      [ [circleCenter_x                                     ,circleCenter_y-0.85*oGridRadius                  , 0     ]  ],
                      [ [circleCenter_x + 0.9*oGridRadius*np.cos(np.pi/8)   ,circleCenter_y-0.9*oGridRadius*np.sin(np.pi/8)   , 0     ]  ],
                      [ [circleCenter_x + 0.9*oGridRadius*np.cos(np.pi/8)   ,circleCenter_y+0.9*oGridRadius*np.sin(np.pi/8)   , 0     ]  ],
                      [ [circleCenter_x                                     ,circleCenter_y+0.85*oGridRadius                  , 0     ]  ],
                      [ [circleCenter_x - 0.85*oGridRadius                  ,circleCenter_y                                   , 0     ]  ] ])
                     
edgePoint= lanMesh.add(edgePoint,zLength,'[:,:,2]+')
edgeType = ['arc']*len(edgePoint)
#-------------------------------------------------------------------------------   
patches=[ [ [0,3],[4,3],[15,3]               ], 
          [ [3,4],[7,4],[10,4],[14,4],[18,4] ],
          [ [9,5],[6,5],[10,3],[12,6],[13,6] ],
          [ [5,5],[9,3],[12,3],[11,6],[8,4]  ],
          [ [0,6],[1,6],[2,6],[3,6]          ],
          [ [15,5],[16,5],[17,5],[18,5]      ] ]    
#------------------------------------------------------------------------------------------------ 
points_solid = np.array([ [xCircle_3,                         yBeam_1,   0],
                          [circleCenter_x + 0.85*oGridRadius, yBeam_1,   0],
                          [xLength_3,                         yBeam_1,   0] ])
points_solid = lanMesh.add(points_solid,beamHeight,'[:,1]+') 
points_solid = lanMesh.add(points_solid,zLength,'[:,2]') 

blocks_solid   = [[0,1,4,3,6,7,10,9],[1,2,5,4,7,8,11,10]]
meshNum_solid  = [[meshNum_around,meshNum_yBeam,1],[meshNum_x3,meshNum_yBeam,1] ]
meshGrad_solid = [[meshGrad_around, 1, 1],[meshGrad_x3, 1, 1] ]

patches_solid = [ [ [0,3] ],
                  [ [0,5],[0,6],[1,5],[1,6],[1,4] ] ]
#------------------------------------------------------------------------------------------------
os.system('rm -rf constant/polyMesh/*')
lanMesh.writeBlockMeshDict(file_read_path,file_write_path,
                           convert,points,blocks,meshNum,meshGrad,  
                           patchType,patchName,patches,
                           edgeType,edgePoint,edgePointId)

os.system('blockMesh')
os.system('foamToVTK')  

os.system('rm -rf constant/solid/polyMesh/*')
lanMesh.writeBlockMeshDict(file_read_path,file_write_path_solid,
                           convert,points_solid,blocks_solid,meshNum_solid,meshGrad_solid,
                           patchType_solid,patchName_solid,patches_solid,
                           [],[],[])
                                                        
os.system('blockMesh -region solid')
os.system('foamToVTK -region solid')

os.system('setSet -batch batch.setSet')
os.system('setsToZones -noFlipMap')
os.system('setSet -region solid -batch batch.setSet')
os.system('setsToZones -region solid -noFlipMap')
