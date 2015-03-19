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
      
      Glyph_sphere = Glyph( GlyphType="Sphere", GlyphTransform="Transform2" )
      Glyph_sphere.GlyphType.ThetaResolution = 50
      Glyph_sphere.GlyphType.PhiResolution = 50
      Glyph_sphere.GlyphType.Radius = Radius
      Show(Glyph_sphere)
     
      my_representation = GetDisplayProperties(Glyph_sphere)
      a1_vel_mag__PVLookupTable = GetLookupTableForArray( "vel_mag_", 1, RGBPoints=[-1.9600000381469727, 0.23, 0.299, 0.754, 0.0, 0.706, 0.016, 0.15] )
      my_representation.ColorArrayName = ('POINT_DATA', 'vel_mag_')
      my_representation.LookupTable = a1_vel_mag__PVLookupTable
         
      ################################################################################
      #View adjust
      RenderView1 = GetRenderView();
      RenderView1.OrientationAxesVisibility = 0;
      RenderView1.CenterAxesVisibility = 0;

      RenderView1.CameraViewUp = [0.0, 1.0, 0.0]
      RenderView1.CameraPosition = [250.00001525878906, 663.1921997070312, 2497.916337989174]
      RenderView1.CameraFocalPoint = [250.00001525878906, 663.1921997070312, -900.3962604270581]
      RenderView1.CameraClippingRange = [2467.722174609282, 2537.992583059012]

      ################################################################################
      Render()

      WriteImage(image_path+'\\'+next(image_filename))
      Delete(Glyph_sphere)
      Delete(sphere)
     

#########################################################################################