from paraview.simple import *
from itertools import count
import string
########################################################################################
#Parameter

Radius=1;
file_number=354;   
                                   
filepath='C:\\Users\\jiabin\\Documents\\MATLAB\\MD_project_2.0\\MD\\one-dimensional\\vtk'
filename = ("particle_%05i.vtk" % i for i in count(1))
image_path='C:\\Users\\jiabin\\Documents\\MATLAB\\MD_project_2.0\\MD\\one-dimensional\\picture'
image_filename=("%05i.png" % i for i in count(1))



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
     """
     #Color the ball by velocity!

     my_representation = GetDisplayProperties(Glyph_sphere)
     a1_vel_y__PVLookupTable = GetLookupTableForArray( "vel_y_", 1, RGBPoints=[-1.9600000381469727, 0.23, 0.299, 0.754, 0.0, 0.706, 0.016, 0.15] )
     my_representation.ColorArrayName = ('POINT_DATA', 'vel_y_')
     my_representation.LookupTable = a1_vel_y__PVLookupTable
     """
     #########################################################################################
     #View adjust

     RenderView = GetRenderView();
     RenderView.OrientationAxesVisibility = 0;
     RenderView.CenterAxesVisibility = 0;

     RenderView = GetRenderView()
     RenderView.CameraPosition = [-151.77348082537276, 50.0, 5.0]
     RenderView.CameraFocalPoint = [43.33397222858568, 50.0, 5.0]
     RenderView.CameraClippingRange = [145.25574601711904, 171.65008303775335]

     Render()

     WriteImage(image_path+'\\'+next(image_filename))
     Delete(Glyph_sphere)
     Delete(sphere)
     
#########################################################################################