from paraview.simple import *
from itertools import count
import random
import string

########################################################################################
#Parameter

N=50;                                                  #Number of sphere
file_number=250;                                       #Number of files
Radius=1./19;                                          #Sphere radius
XLength=1;                                             #box Length in X direction
YLength=1;                                             #box Length in y direction
ZLength=5;                                             #box Length in Z direction

########################################################################################
#Create spheres

sphere=[];
for i in range(N):
    sphere.append(Sphere());
    sphere[i].Radius=Radius;
    sphere[i].ThetaResolution=30;
    sphere[i].PhiResolution=30;
    sphere_dp=GetDisplayProperties(sphere[i]);
    sphere_dp.DiffuseColor=[random.random(),random.random(),random.random()];
    sphere_dp.Opacity=0.6;
    Show(sphere[i]);

########################################################################################
#Create box

box=Box();
box.XLength=XLength;
box.YLength=YLength;
box.ZLength=ZLength;
box.Center=[XLength/2.0,YLength/2.0,ZLength/2.0];
Show(box);
box_dp=GetDisplayProperties(box);
box_dp.Opacity=0.45;

#########################################################################################
#View adjust

RenderView = GetRenderView();
RenderView.OrientationAxesVisibility = 0;
RenderView.CenterAxesVisibility = 0;
RenderView.CameraPosition=[-0.7836256180045292, 3.0398714885700127, 3.2935426321543697];

#########################################################################################
#Read files

filename = ("pos_%05i" % i for i in count(1))
image_filename=("%05i.png" % i for i in count(1))

while file_number:
    
    file_number=file_number-1;
    pos_files=open(next(filename));
    
    str=pos_files.readlines();
    pos=[[0]*3]*N;

    for i in range(N):
        temp=str[i+1].split();
        pos[i]=[float(temp[0]),float(temp[1]),float(temp[2])];

    pos_files.close();
#########################################################################################
#Move spheres and save image 
  
    for i in range(N):
        sphere[i].Center=pos[i];  

    Render();
    WriteImage(next(image_filename))

#########################################################################################
