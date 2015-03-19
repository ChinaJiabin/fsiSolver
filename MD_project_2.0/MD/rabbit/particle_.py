from paraview.simple import *
from itertools import count
import string
########################################################################################
#Parameter

Radius=0.5;
file_number=70;   
                                   
filepath='C:\\Users\\jiabin\\Documents\\MATLAB\\MD_project_2.0\\MD\\rabbit\\vtk'
filename = ("particle_%05i.vtk" % i for i in count(1))
image_path='C:\\Users\\jiabin\\Documents\\MATLAB\\MD_project_2.0\\MD\\rabbit\\picture'
image_filename=("%05i.png" % i for i in count(1))

#########################################################################################
#View adjust

RenderView = GetRenderView();
RenderView.OrientationAxesVisibility = 0;
RenderView.CenterAxesVisibility = 0;

RenderView.CameraViewUp = [0.0, 1.0, 0.0]
RenderView.CameraFocalPoint = [-366.9905325328733, 1026.0664644773592, -3440.96229960942]
RenderView.CameraClippingRange = [262.94302774855396, 277.5371951159417]
RenderView.CameraPosition = [-366.9905325328733, 1026.0664644773592, 270.86669469550907]

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

     DataRepresentation_wall=Show(wall)
     DataRepresentation_wall.Representation= 'Surface With Edges'
     DataRepresentation1=Show(sphere)

     a1_vel_mag_PVLookupTable = GetLookupTableForArray( "vel_mag", 1, RGBPoints=[9604.0, 0.23, 0.299, 0.754, 9604.0, 0.706, 0.016, 0.15], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0, AllowDuplicateScalars=1 )
     a1_vel_mag_PiecewiseFunction = CreatePiecewiseFunction( Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0] )
     
     DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
     DataRepresentation1.SelectionPointFieldDataArrayName = 'vel_mag'
     DataRepresentation1.ScalarOpacityFunction = a1_vel_mag_PiecewiseFunction
     DataRepresentation1.ColorArrayName = ('POINT_DATA', 'vel_mag')
     DataRepresentation1.ScalarOpacityUnitDistance = 196.69573026281554
     DataRepresentation1.LookupTable = a1_vel_mag_PVLookupTable
     DataRepresentation1.ScaleFactor = 114.86399230957032

     """
     sphere_dp = GetActiveSource()
     Glyph_sphere = Glyph( GlyphType="Sphere", GlyphTransform="Transform2" )
     Glyph_sphere.GlyphType.ThetaResolution = 50
     Glyph_sphere.GlyphType.PhiResolution = 50
     Glyph_sphere.GlyphType.Radius = Radius
     Show(Glyph_sphere)
     """
     ###############################################################################
     """
     #Color the ball by velocity!

     my_representation = GetDisplayProperties(Glyph_sphere)
     a1_vel_mag__PVLookupTable = GetLookupTableForArray( "vel_mag_", 1, RGBPoints=[-1.9600000381469727, 0.23, 0.299, 0.754, 0.0, 0.706, 0.016, 0.15] )
     my_representation.ColorArrayName = ('POINT_DATA', 'vel_mag_')
     my_representation.LookupTable = a1_vel_mag__PVLookupTable
     """
     ################################################################################

     Render()

     WriteImage(image_path+'\\'+next(image_filename))
     #Delete(Glyph_sphere)
     Delete(sphere)
#########################################################################################