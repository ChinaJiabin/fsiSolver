#!/usr/bin/vtkpython
import math
import os

datapath_write=os.getcwd()+'/constant/time-series'
file_write=open(datapath_write,'w')

time      = 0
deltaTime = 0.0001

file_write.write("(\n")

while (time-0.01)<0: 
 
      if time <= 0.003:
         file_write.write('('+str(time)+' 4 )\n')
      else:
         file_write.write('('+str(time)+' 0 )\n')

      time+=deltaTime 
    
file_write.write(")\n")

file_write.close()

