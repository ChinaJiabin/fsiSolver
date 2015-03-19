%Geometry Parameter
 %-------------------------------------------------------------------------
%Geometry Parameter
 %-------------------------------------------------------------------------
 %For paraview 
 
 width=235;
 height=235;
 length_=960;
 exit_w=20;
 exit_h=10;
x_paraview=kron([
                 0             
                 width/2-sqrt(3)*height/6-50*sqrt(3)/3
                 width/2-sqrt(3)*height/6+50*sqrt(3)/3
                 width/2+sqrt(3)*height/6-50*sqrt(3)/3
                 width/2+sqrt(3)*height/6+50*sqrt(3)/3
                 width
                 ],                                     ...
                 ones(4,1));
y_paraview=height*ones(24,1);
z_paraview=kron(ones(6,1),[0,0.25,3.25,3.5]');

points_wall=[x_paraview,y_paraview,z_paraview];
points_wall=[ points_wall
             %points_wall+[zeros(24,1),-height+(width-x_paraview)*tan(pi/15)+exit_h,zeros(24,1)]
              points_wall+[zeros(24,1),-height+(width-x_paraview)*tan(pi/15),zeros(24,1)]
            ];
points_wall=[
             points_wall;
             width/2-sqrt(3)*height/6-length_/2-50*sqrt(3)/3,height+sqrt(3)*length_/2,0.25
             width/2-sqrt(3)*height/6-length_/2-50*sqrt(3)/3,height+sqrt(3)*length_/2,3.25
             width/2-sqrt(3)*height/6-length_/2+25*sqrt(3)/3,height+sqrt(3)*length_/2+25,0.25
             width/2-sqrt(3)*height/6-length_/2+25*sqrt(3)/3,height+sqrt(3)*length_/2+25,3.25
             width/2+sqrt(3)*height/6+length_/2-25*sqrt(3)/3,height+sqrt(3)*length_/2+25,0.25
             width/2+sqrt(3)*height/6+length_/2-25*sqrt(3)/3,height+sqrt(3)*length_/2+25,3.25
             width/2+sqrt(3)*height/6+length_/2+50*sqrt(3)/3,height+sqrt(3)*length_/2,0.25
             width/2+sqrt(3)*height/6+length_/2+50*sqrt(3)/3,height+sqrt(3)*length_/2,3.25
            % width+exit_w,exit_h,0
            % width+exit_w,exit_h,3.5
            % width+exit_w,0,0
            % width+exit_w,0,3.5
            ];

%cell_wall=([1:20,25:44])';
cell_wall=(1:20)';
cell_wall=cell_wall(mod(cell_wall,4)~=0);
cell_wall=[cell_wall,cell_wall+1];
cell_wall=[cell_wall,fliplr(cell_wall)+4];
cell_wall=[cell_wall,cell_wall+24]-1;
%cell_wall=[8*ones(30,1),cell_wall];
cell_wall=[8*ones(15,1),cell_wall];
cell_wall=[
           cell_wall;
          % 8 72 73 75 74 5 6 10 9
          % 8 76 77 79 78 13 14 18 17
          % 8 45 46 81 80 69 70 83 82
            8 48 49 51 50 5 6 10 9
            8 52 53 55 54 13 14 18 17
          ];

N_points_wall=size(points_wall,1);
N_cell_wall=size(cell_wall,1);
%--------------------------------------------------------------------------
[Nw,Pw,Nw_cell,N_empty_wall, Nw_empty,faces]=parameter_mesh(points_wall,cell_wall);
%[Nw,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_wall_change(Nw,Pw,Nw_cell,N_empty_wall,Nw_empty,29); 
 
 
 
 
 
 
 
 
 
 
 
 