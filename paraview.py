########################################################################### #mag(U)
#1.Create new arrays                                                        #curl(U) 
normals = inputs[0].PointData['Normals']                                    #area(input[0])
output.PointData.append(normals[:,0], "Normals_x")                          #inputs[0].Points[:,1]
#--------------------------------------------------------------------------
colors = vtk.vtkUnsignedCharArray();
colors.SetNumberOfComponents(3);
colors.SetName("colors");

numPoints = input.GetNumberOfPoints()
for i in range(numPoints):
    colors.InsertNextTuple3(i,0,0);

output.GetPointData().AddArray(colors)
########################################################################### 
#2.Adjust coordinates of points 
input=inputs[0]

newPoints=vtk.vtkPoints()
numPoints=input.GetNumberOfPoints()

for i in range(numPoints):
    x,y,z=input.GetPoint(i)
    newPoints.InsertPoint(i, x, y, 1 + z*0.3)

output.SetPoints(newPoints)
#--------------------------------------------------------------------------
from paraview.vtk.dataset_adapter import numpyTovtkDataArray

input = inputs[0]

newPoints = vtk.vtkPoints()

zs = 1 + input.Points[:,2]*0.3
coords = hstack([input.Points[:,0:2],zs])
newPoints.SetData(numpyTovtkDataArray(coords))

output.SetPoints(newPoints)
###########################################################################
#3.Deal with multiple inputs
output.PointData.append(inputs[1].PointData['p']-inputs[0].PointData['p'],
                       "difference")
###########################################################################
#4.vtkTable
rtdata = inputs[0].PointData['RTData']
output.RowData.append(min(rtdata), 'min')
output.RowData.append(max(rtdata), 'max')
###########################################################################
#5.CSV Reader(Source)
#file format:
# x,y,z,velocity
# 1,0,0,1
# 2,0,1,1
# . . .

from paraview import vtk
import os

filepath="C:\\Users\\jiabin\\Documents\\MATLAB\\python_script\\datafile.txt"
filename=os.path.normcase(filepath)

pts=vtk.vtkPoints()
f=open(filename)
pdo=self.GetOutput()

firstline=True
for line in f:
  if firstline:
    firstline=False
    for pos,word in enumerate(line.split(",")):
      if pos > 2:
        newArray = vtk.vtkDoubleArray()
        newArray.SetName(word)
        newArray.SetNumberOfComponents(1)
        pdo.GetPointData().AddArray(newArray)
  else:
    for pos,word in enumerate(line.split(",")):
      print word
      if pos == 0:
        x = float(word)
      if pos == 1:
        y = float(word)
      if pos == 2:
        z = float(word)
      if pos > 2:
        array = pdo.GetPointData().GetArray(pos-3)
        array.InsertNextValue(float(word))
    pts.InsertNextPoint(x,y,z)
pdo.SetPoints(pts)
###########################################################################
#6.Create vtkPolyData
import math

numPts = 80
length = 8
rounds = 2

pdo = self.GetPolyDataOutput()
newPts = vtk.vtkPoints()

vals1 = vtk.vtkDoubleArray()
vals1.SetName('First Property')
vals2 = vtk.vtkDoubleArray()
vals2.SetName('Second Property') 

for i in range(numPts):
   x = i*length/numPts
   y = math.sin(i*rounds*2*math.pi/numPts)
   z = math.cos(i*rounds*2*math.pi/numPts)
   newPts.InsertPoint(i,x,y,z)
 
   vals1.InsertNextValue(i)
   vals2.InsertNextValue(math.sin(i*2.0*math.pi/numPts)) 

pdo.SetPoints(newPts)

pdo.GetPointData().SetScalars(vals1)
pdo.GetPointData().AddArray(vals2)   

aPolyLine = vtk.vtkPolyLine()
aPolyLine.GetPointIds().SetNumberOfIds(numPts)
for i in range(numPts):
    #Add the points to the line. The first value indicates
    #the order of the point on the line. The second value
    #is a reference to a point in a vtkPoints object. Depends
    #on the order that Points were added to vtkPoints object.
    #Note that this will not be associated with actual points
    #until it is added to a vtkPolyData object which holds a
    #vtkPoints object.
   aPolyLine.GetPointIds().SetId(i, i)
pdo.Allocate(1, 1)
pdo.InsertNextCell(aPolyLine.GetCellType(), aPolyLine.GetPointIds())
#########################################################################
