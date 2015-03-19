from paraview.simple import *
from itertools import count
import string
########################################################################################
#Parameter

Radius=1;
N_star_file=800;
file_number=579;   
                                   
filepath='C:\\Users\\jiabin\\Documents\\MATLAB\\MD_project_2.0\\MD\\rabbit\\vtk'
filename = ("particle_%05i.vtk" % i for i in count(N_star_file))
image_path='C:\\Users\\jiabin\\Documents\\MATLAB\\MD_project_2.0\\MD\\rabbit\\picture'
image_filename=("%05i.png" % i for i in count(N_star_file))

########################################################################################
#Create wall
wall=LegacyVTKReader( FileNames=[filepath+'\\wall.vtk'] )
wall_dp=GetActiveSource()
wall_dp=GetDisplayProperties(wall_dp)
wall_dp.Representation='Surface With Edges'
wall_dp.Opacity=0.4;

########################################################################################
#Create spheres

while file_number:
      file_number=file_number-1;
      sphere=LegacyVTKReader( FileNames=[filepath+'\\'+next(filename)] )

      Show(wall)
      Show(sphere)

      ###############################################################################
      #Color the ball by velocity!
      sphere_dp = GetActiveSource()
      """
      Glyph_sphere = Glyph( GlyphType="Sphere", GlyphTransform="Transform2" )
      Glyph_sphere.GlyphType.ThetaResolution = 50
      Glyph_sphere.GlyphType.PhiResolution = 50
      Glyph_sphere.GlyphType.Radius = Radius
      Show(Glyph_sphere)
     
      my_representation = GetDisplayProperties(Glyph_sphere)
      a1_vel_y__PVLookupTable = GetLookupTableForArray( "vel_y_", 1, RGBPoints=[-1.9600000381469727, 0.23, 0.299, 0.754, 0.0, 0.706, 0.016, 0.15] )
      my_representation.ColorArrayName = ('POINT_DATA', 'vel_y_')
      my_representation.LookupTable = a1_vel_y__PVLookupTable
      """
      Glyph_sphere=Glyph( GlyphType="Arrow", GlyphTransform="Transform2" )
      Glyph_sphere.SetScaleFactor = 0.008
      Glyph_sphere.Scalars = ['POINTS', 'vel_mag']
      Glyph_sphere.Vectors = ['POINTS', 'velocity']
      Glyph_sphere.GlyphTransform.Scale = [0.1, 0.1, 0.1]

      my_representation=Show(Glyph_sphere)
      my_representation.ColorArrayName = ('POINT_DATA', 'vel_mag')
      my_representation.ScaleFactor = 40.475990295410156
      my_representation.SelectionPointFieldDataArrayName = 'vel_mag'
      my_representation.EdgeColor = [0.0, 0.0, 0.5000076295109483]

      a1_vel_mag_PVLookupTable = GetLookupTableForArray( "vel_mag", 1,RGBPoints=[-1.9600000381469727, 0.23, 0.299, 0.754, 0.0, 0.706, 0.016, 0.15]  )
      my_representation.LookupTable = a1_vel_mag_PVLookupTable

      ################################################################################
      #View adjust
      RenderView1 = GetRenderView();
      RenderView1.OrientationAxesVisibility = 0;
      RenderView1.CenterAxesVisibility = 0;

      RenderView1.CameraFocalPoint = [250, 290, -3317]
      RenderView1.CameraClippingRange = [75, 85]
      RenderView1.CameraPosition = [250, 290, 81]

      ################################################################################
      Render()

      WriteImage(image_path+'\\'+next(image_filename))
      Delete(Glyph_sphere)
      Delete(sphere)
     

#########################################################################################