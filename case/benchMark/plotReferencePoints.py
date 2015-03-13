import os
import re
file_path_read      = 'logFsi'
file_read           = open(file_path_read, 'r')

file_path_write     = 'plot/referencePointDisplacement.csv'
file_write          = open(file_path_write,'w')

file_write.write('time,x_displacement,y_displacement\n') 

time = '0' 

for l in file_read:
  
  if l[0:15]=='X displacement:':
    displacement = time+','+l[15:-1]+','
  if l[0:15]=='Y displacement:':
    file_write.write(displacement+l[15:-1]+'\n')
    time = str(float(time)+0.001)

file_read.close()
file_write.close()

















'''
timestep = 0.02
stepUnit = 50

file_path_write = 'plot/referencePointDisplacement.csv'
file_write = open(file_path_write,'w')
file_write.write('time,x_displacement,y_displacement\n')
file_write.write('0,0,0\n')
#---------------------------------------------------------------------------- 
#Find reference point id
referencePoint = '(0.6 0.2 0)\n'
file_path_read = 'constant/solid/polyMesh/points'
file_read = open(file_path_read, 'r')
lines = file_read.readlines()
for points_id,l in enumerate(lines[20:]):
    if l == referencePoint:
       referencePoint_id = points_id
       break

file_read.close()
#---------------------------------------------------------------------------- 
referencePoint = referencePoint.replace('(','') 
referencePoint = referencePoint.replace(')','') 
referencePoint = referencePoint.replace('\n','') 
referencePoint = referencePoint.split(' ')

file_num=0
while True: 

   file_num+=1
   if file_num%stepUnit:
      file_path_read = str(file_num*timestep)+'/solid/polyMesh/points'
   else:
      file_path_read = str(file_num/stepUnit)+'/solid/polyMesh/points'

   if os.path.isfile(file_path_read) == False:
      break

   file_read = open(file_path_read, 'r')

   lines = file_read.readlines()
   point = lines[20+referencePoint_id]

   point = point.replace('(','') 
   point = point.replace(')','') 
   point = point.replace('\n','') 
   point = point.split(' ')

   file_write.write(str(file_num*timestep)+',')
   file_write.write(str( float(point[0])-float(referencePoint[0]) )+',')
   file_write.write(str( float(point[1])-float(referencePoint[1]) )+'\n')
   
   file_read.close()

file_write.close()
'''
#---------------------------------------------------------------------------- 
