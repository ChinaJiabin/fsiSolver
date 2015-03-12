import os
import copy
import numpy as np

def add(x,value,transform,flag='v'):
    temp = copy.deepcopy(x)
    exec('temp'+transform+'=value')
    if flag=='h':
       return np.hstack((x,temp))
    return np.vstack((x,temp))  

def rotPoints(points, degree, axis):
  if axis == 'z':
    return np.dot( points, np.array( [ [ np.cos(degree), np.sin(degree), 0],
                                       [-np.sin(degree), np.cos(degree), 0],
                                       [              0,              0, 1] ]) )
  if axis == 'y':
    return np.dot( points, np.array( [ [ np.cos(degree), 0, np.sin(degree)],
                                       [-np.sin(degree), 0, np.cos(degree)],
                                       [              0, 1,             0] ]) )  
  if axis == 'x':
    return np.dot( points, np.array( [ [ 0,  np.cos(degree), np.sin(degree)],
                                       [ 0, -np.sin(degree), np.cos(degree)],
                                       [ 1,               0,              0] ]) )   

class mesh:

#     y
#     |
#     |
#     |__ __ __ x
#    / 
#   /
#  /
# z             front       bebind      left        right       top         bottom
#unitFaceDict={1:[4,5,6,7],2:[0,3,2,1],3:[0,4,7,3],4:[1,2,6,5],5:[2,3,7,6],6:[1,5,4,0]}

  unitFaceDict={ 1:[4,5,6,7], 2:[0,3,2,1],
                 3:[0,4,7,3], 4:[1,2,6,5],
                 5:[2,3,7,6], 6:[1,5,4,0] }

  def __init__(self, points,   blocks, 
                     meshNum,  meshGrad,
                     edgePointsId = [], edgePoints = [], edgeType = [],
                     patchType    = [], patchName  = [], patches  = [], convert = 1):
    
    self.points = points
    self.blocks = blocks
    self.convert = convert

    self.meshNum = meshNum
    self.meshGrad = meshGrad

    self.patchType = patchType
    self.patchName = patchName
    self.patches = patches
   
    self.edgeType = edgeType
    self.edgePoints = edgePoints
    self.edgePointsId = edgePointsId

  def write(self):
        
    file_read = open('/opt/foam/foam-extend-3.1/lanMesh/blockMeshDict_model', 'r')
    file_write= open(os.getcwd()+'/constant/polyMesh/blockMeshDict','w')

    N_blocks=len(self.blocks)
    lines_model=file_read.readlines()
    #Header
    for line in lines_model[0:16]:
	file_write.write(line)

    #convertToMeters
    file_write.write('convertToMeters '+str(self.convert)+';\n')

    #vertices
    for line in lines_model[17:20]:
	file_write.write(line)
    for point in self.points:
	file_write.write('( ')
	for i in range(3):
	    file_write.write(str(point[i])+' ')
	file_write.write(')\n')

    #blocks
    for line in lines_model[20:24]:
	file_write.write(line)
    for i in range(N_blocks):
	file_write.write('hex ( ')
	for j in range(8):
	    file_write.write(str(self.blocks[i][j])+' ')
	file_write.write(') (')
	for j in range(3):
	    file_write.write(str(self.meshNum[i][j])+' ')                          
	file_write.write(') simpleGrading ( ')
	for j in range(3):
	    file_write.write(str(self.meshGrad[i][j])+' ')
	file_write.write(')\n')

    #edges
    edgeNum = len(self.edgeType)
    for line in lines_model[24:28]:
	file_write.write(line)
    for i in range(edgeNum):
	file_write.write(self.edgeType[i]+' ')
	for j in self.edgePointsId[i]:
	    file_write.write(str(j)+' ')
	for edge in self.edgePoints[i]:   
	    file_write.write('(')
	    for j in edge:
		file_write.write(str(j)+' ')
	    file_write.write(') ')
	file_write.write('\n')
    #patches
    patchNum=len(self.patches)
    for line in lines_model[28:32]:
	file_write.write(line)
    for i in range(patchNum):
	file_write.write(self.patchType[i]+' '+self.patchName[i]+'\n')
	file_write.write('(\n')
	for face in self.patches[i]:
		file_write.write('( ')
		for j in mesh.unitFaceDict[face[1]]:
		    file_write.write(str(self.blocks[face[0]][j])+' ')
		file_write.write(')\n')
	file_write.write(')\n\n')

    #mergePatchPairs
    for line in lines_model[32:36]:
	file_write.write(line)

    file_write.write(');\n')
    file_write.write('\n// ************************************************************************* //')

    file_write.close();
    file_read.close();

def createRectangle(width,hight,unitLen,thickness=0.01):
  points = np.array( [ [0,         0, 0],
                       [width,     0, 0],
                       [width, hight, 0],
                       [0    , hight, 0] ] )
  points = add(points, thickness, '[:,2]')
 
  blocks =  [ range(0,8) ]
  meshNum = [ [int(width/unitLen),int(hight/unitLen),1] ]
  return mesh(points, blocks, meshNum, [[1,1,1]])

def createCube(width,hight,thickness,unitLen):
#     y:hight
#     |
#     |
#     |__ __ __ x:width
#    / 
#   /
#  /
# z:thickness
  points = np.array( [ [    0,     0, 0],
                       [width,     0, 0],
                       [width, hight, 0],
                       [    0, hight, 0] ] )
  points = add(points, thickness, '[:,2]')

  blocks =  [ range(0,8) ]
  meshNum = [ [int(width/unitLen),int(hight/unitLen),int(thickness/unitLen)] ]
  return mesh(points, blocks, meshNum, [[1,1,1]])

def createCircle(radius, unitLen, meshGradT = 2, meshRatio = 0.8, oGridRatio = [0.6, 0.5], hight = 0.01):
  points = np.array( [ [ radius,       0, 0],
                       [      0,  radius, 0],
                       [-radius,       0, 0],
                       [      0, -radius, 0] ] )      
  points = add(points, oGridRatio[0], '*')  
  points = add(points, hight, '[:,2]')  
      
  blocks = np.array( [ [0,1,5,4],[1,2,6,5],[2,3,7,6],[3,0,4,7],[4,5,6,7] ] )
  blocks = add(blocks, len(points)/2, '+', 'h')
  
  meshH = 1
  meshR = int(np.sqrt(2)*radius*oGridRatio[0]/unitLen*meshRatio)
  meshT = int((1-oGridRatio[0])*radius/unitLen)

  meshNum  = np.vstack( [ (len(blocks)-1)*[[meshR, meshT, meshH]],[meshR, meshR, meshH] ] )
  meshGrad = np.vstack( [ (len(blocks)-1)*[[1,meshGradT,1]]      ,[1,1,1] ] )

  edgePointsId = np.array( [ [0,1],[1,2],[2,3],[3,0] ] )
  edgePointsId = add(edgePointsId, len(points)/4, '+')
  edgePointsId = add(edgePointsId, len(points)/2, '+')

  edgePoints = np.array( [ [ [  np.sqrt(0.5)*radius,  np.sqrt(0.5)*radius, 0] ],
                           [ [ -np.sqrt(0.5)*radius,  np.sqrt(0.5)*radius, 0] ],
                           [ [ -np.sqrt(0.5)*radius, -np.sqrt(0.5)*radius, 0] ],
                           [ [  np.sqrt(0.5)*radius, -np.sqrt(0.5)*radius, 0] ] ] )
  edgePoints = add(edgePoints, oGridRatio[1], '*')
  edgePoints = add(edgePoints, hight, '[:,:,2]') 
  edgeType = ['arc']*len(edgePoints)
  
  return mesh(points, blocks, meshNum, meshGrad, edgePointsId, edgePoints, edgeType)

def createCylinder(radius,hight,unitLen, meshGradT = 2, meshRatio = 0.8, oGridRatio = [0.6, 0.5]):
  points = np.array( [ [ radius,       0, 0],
                       [      0,  radius, 0],
                       [-radius,       0, 0],
                       [      0, -radius, 0] ] )      
  points = add(points, oGridRatio[0], '*')  
  points = add(points, hight, '[:,2]')  
      
  blocks = np.array( [ [0,1,5,4],[1,2,6,5],[2,3,7,6],[3,0,4,7],[4,5,6,7] ] )
  blocks = add(blocks, len(points)/2, '+', 'h')
  
  meshH = int(hight/unitLen)
  meshR = int(np.sqrt(2)*radius*oGridRatio[0]/unitLen*meshRatio)
  meshT = int((1-oGridRatio[0])*radius/unitLen)

  meshNum  = np.vstack( [ (len(blocks)-1)*[[meshR, meshT, meshH]],[meshR, meshR, meshH] ] )
  meshGrad = np.vstack( [ (len(blocks)-1)*[[1,meshGradT,1]]      ,[1,1,1] ] )

  edgePointsId = np.array( [ [0,1],[1,2],[2,3],[3,0] ] )
  edgePointsId = add(edgePointsId, len(points)/4, '+')
  edgePointsId = add(edgePointsId, len(points)/2, '+')

  edgePoints = np.array( [ [ [  np.sqrt(0.5)*radius,  np.sqrt(0.5)*radius, 0] ],
                           [ [ -np.sqrt(0.5)*radius,  np.sqrt(0.5)*radius, 0] ],
                           [ [ -np.sqrt(0.5)*radius, -np.sqrt(0.5)*radius, 0] ],
                           [ [  np.sqrt(0.5)*radius, -np.sqrt(0.5)*radius, 0] ] ] )
  edgePoints = add(edgePoints, oGridRatio[1], '*')
  edgePoints = add(edgePoints, hight, '[:,:,2]') 
  edgeType = ['arc']*len(edgePoints)
  
  return mesh(points, blocks, meshNum,  meshGrad, edgePointsId, edgePoints, edgeType)

def createBall(radius, unitLen, oGridRatio = 0.8):
  points = np.array([ [  np.sqrt(1./3)*radius,  np.sqrt(1./3)*radius, -np.sqrt(1./3)*radius],
                      [ -np.sqrt(1./3)*radius,  np.sqrt(1./3)*radius, -np.sqrt(1./3)*radius],
                      [ -np.sqrt(1./3)*radius, -np.sqrt(1./3)*radius, -np.sqrt(1./3)*radius],
                      [  np.sqrt(1./3)*radius, -np.sqrt(1./3)*radius, -np.sqrt(1./3)*radius] ])
  points = add(points, np.sqrt(0.5)*radius, '[:,2]')
  points = add(points, oGridRatio, '*')

  blocks = np.array( [ [4,5,6,7], [0,3,2,1], [0,4,7,3] ,[1,2,6,5] ,[2,3,7,6] ,[1,5,4,0] ] )
  blocks = add(blocks, len(points)/2, '+', 'h')
  #blocks = np.vstack([blocks,range(8,16)])
  
  edgePointsId = np.array( [ [0,1],[1,2],[2,3],[3,0],
                             [4,5],[5,6],[6,7],[7,4] ] )
  edgePoints = np.array( [ [ [                    0,  np.sqrt(0.5)*radius, -np.sqrt(0.5)*radius ] ],
                           [ [ -np.sqrt(0.5)*radius,                    0, -np.sqrt(0.5)*radius ] ],
                           [ [                    0, -np.sqrt(0.5)*radius, -np.sqrt(0.5)*radius ] ],
                           [ [  np.sqrt(0.5)*radius,                    0, -np.sqrt(0.5)*radius ] ] ] )
  edgeType = ['arc']*len(edgePoints)

  return mesh(points, blocks, len(blocks)*[[2,2,2]], len(blocks)*[[1,1,1]], edgePointsId, edgePoints, edgeType)
