from paraview.simple import *
from itertools import count
import string
########################################################################################
#Parameter

Radius=2;
file_number=269;   
                                   
filepath='C:\\Users\\jiabin\\Documents\\MATLAB\\MD_project_2.0\\MD\\three-dimensional\\vtk'
filename = ("particle_%05i.vtk" % i for i in count(1))
image_path='C:\\Users\\jiabin\\Documents\\MATLAB\\MD_project_2.0\\MD\\three-dimensional\\picture'
image_filename=("%05i.png" % i for i in count(1))

#########################################################################################
#View adjust

RenderView = GetRenderView();
RenderView.OrientationAxesVisibility = 0;
RenderView.CenterAxesVisibility = 0;

#RenderView.CameraViewUp = [0.1696482661098314, 0.827966104764239, -0.5345012583403905]
#RenderView.CameraFocalPoint = [335.5279473465183, 549.0289836957569, -142.90866308092194]
#RenderView.CameraClippingRange = [1372.2172425975807, 3590.2127705837042]
#RenderView.CameraPosition = [-546.6786095604552, 2007.8425984231885, 1836.8498443518622]

RenderView.CameraViewUp = [0.0, 1.0, 0.0]
RenderView.CameraFocalPoint = [-366.9905325328733, 1026.0664644773592, -3440.96229960942]
RenderView.CameraClippingRange = [262.94302774855396, 277.5371951159417]
RenderView.CameraPosition = [-366.9905325328733, 1026.0664644773592, 270.86669469550907]

RenderView.CameraPosition = [91.0, 117.5, 576.0048862833432]
RenderView.CameraFocalPoint = [91.0, 117.5, 1.75]

########################################################################################
#Create wall
wall=LegacyVTKReader( FileNames=[filepath+'\\wall.vtk'] )
wall_dp=GetActiveSource()
wall_dp=GetDisplayProperties(wall_dp)
wall_dp.Opacity=0.4;

########################################################################################
#Create spheres

while file_number:
     file_number=file_number-1;
     sphere=LegacyVTKReader( FileNames=[filepath+'\\'+next(filename)] )

     Show(wall)
     Show(sphere)
     sphere_dp = GetActiveSource()
     Glyph_sphere = Glyph( GlyphType="Sphere", GlyphTransform="Transform2" )
     Glyph_sphere.GlyphType.ThetaResolution = 50
     Glyph_sphere.GlyphType.PhiResolution = 50
     Glyph_sphere.GlyphType.Radius = Radius
     Show(Glyph_sphere)
     
     ###############################################################################
     #Color the ball by velocity!

     #my_representation = GetDisplayProperties(Glyph_sphere)
     #a1_vel_y__PVLookupTable = GetLookupTableForArray( "vel_y_", 1, RGBPoints=[-1.9600000381469727, 0.23, 0.299, 0.754, 0.0, 0.706, 0.016, 0.15] )
     #my_representation.ColorArrayName = ('POINT_DATA', 'vel_y_')
     #my_representation.LookupTable = a1_vel_y__PVLookupTable

     ################################################################################

     Render()

     WriteImage(image_path+'\\'+next(image_filename))
     Delete(sphere)
     Delete(Glyph_sphere)

#########################################################################################