%Geometry Parameter 
%-------------------------------------------------------------------------
high_wall=100;
points_wall=[ 
              0   high_wall 0
              0   high_wall 10
              10  high_wall 10
              10  high_wall 0
              0   0         0
              0   0         10
              10  0         10
              10  0         0          
             ];
cell_wall=[
           8 0 1 2 3 4 5 6 7
           ];
       
 
[Nw,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_mesh(points_wall,cell_wall);
N_points_wall=size(points_wall,1);
N_cell_wall=size(cell_wall,1);
%-------------------------------------------------------------------------
 
 