%Geometry Parameter
 %-------------------------------------------------------------------------
%Geometry Parameter
 %-------------------------------------------------------------------------
 %For paraview 
 
 width=500;
 height=470;
 thickness=3.5;
 floor_angle=pi/15;
 pole_distance=80;
 pole_length=960;
 pole_width=50;
 pole_angle=pi/3;
 
 statistical_area_width=40;
 statistical_area_height=40;
 statistical_area_top=160;
 
x_paraview=kron([
                 0             
                 width/2-pole_distance/2-pole_width/cos(pole_angle/2)
                 width/2-pole_distance/2
                 width/2-statistical_area_width/2
                 width/2+statistical_area_width/2
                 width/2+pole_distance/2
                 width/2+pole_distance/2+pole_width/cos(pole_angle/2)
                 width
                 ],                                     ...
                 [1;1]);
y_paraview=height*ones(16,1);
z_paraview=kron(ones(8,1),[0,thickness]');

points_wall=[x_paraview,y_paraview,z_paraview];
points_wall=[ points_wall;
              points_wall+repmat([0,-statistical_area_top,0],16,1);
              points_wall+repmat([0,-statistical_area_top-statistical_area_height,0],16,1);
              points_wall+[zeros(16,1),-height+(width-x_paraview)*tan(floor_angle),zeros(16,1)];
            ];
points_wall=[
             points_wall
             width/2-pole_distance/2-pole_width/cos(pole_angle/2)-pole_length*sin(pole_angle/2),height+pole_length*cos(pole_angle/2),0
             width/2-pole_distance/2-pole_width/cos(pole_angle/2)-pole_length*sin(pole_angle/2),height+pole_length*cos(pole_angle/2),thickness
             width/2-pole_distance/2-pole_width/cos(pole_angle/2)-pole_length*sin(pole_angle/2)+pole_width*cos(pole_angle/2),height+pole_length*cos(pole_angle/2)+pole_width*sin(pole_angle/2),0
             width/2-pole_distance/2-pole_width/cos(pole_angle/2)-pole_length*sin(pole_angle/2)+pole_width*cos(pole_angle/2),height+pole_length*cos(pole_angle/2)+pole_width*sin(pole_angle/2),thickness
             width/2+pole_distance/2+pole_width/cos(pole_angle/2)+pole_length*sin(pole_angle/2)-pole_width*cos(pole_angle/2),height+pole_length*cos(pole_angle/2)+pole_width*sin(pole_angle/2),0
             width/2+pole_distance/2+pole_width/cos(pole_angle/2)+pole_length*sin(pole_angle/2)-pole_width*cos(pole_angle/2),height+pole_length*cos(pole_angle/2)+pole_width*sin(pole_angle/2),thickness
             width/2+pole_distance/2+pole_width/cos(pole_angle/2)+pole_length*sin(pole_angle/2),height+pole_length*cos(pole_angle/2),0
             width/2+pole_distance/2+pole_width/cos(pole_angle/2)+pole_length*sin(pole_angle/2),height+pole_length*cos(pole_angle/2),thickness
            ];

cell_wall=(1:14)';
cell_wall=cell_wall(mod(cell_wall,2)~=0);
cell_wall=[cell_wall,cell_wall+1,cell_wall+3,cell_wall+2];
cell_wall=[cell_wall,cell_wall+16];
cell_wall=[cell_wall;cell_wall+16;cell_wall+32]-1;
cell_wall=[8*ones(size(cell_wall,1),1),cell_wall];
cell_wall=[
           cell_wall;
           8 64 65 67 66 2 3 5 4
           8 68 69 71 70 10 11 13 12
          ];

N_points_wall=size(points_wall,1);
N_cell_wall=size(cell_wall,1);
%--------------------------------------------------------------------------
[Nw,Pw,Nw_cell,N_empty_wall, Nw_empty,faces]=parameter_mesh(points_wall,cell_wall);
[Nw,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_wall_change(Nw,Pw,Nw_cell,N_empty_wall,Nw_empty,12); 
[Nw,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_wall_change(Nw,Pw,Nw_cell,N_empty_wall,Nw_empty,13); 
[Nw,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_wall_change(Nw,Pw,Nw_cell,N_empty_wall,Nw_empty,14); 
%--------------------------------------------------------------------------
 
 
 
 
 
 
 
 
 
 
 
 