%Geometry Parameter
 %-------------------------------------------------------------------------
 %{
points_wall=[ 0 1 0
              0 1 1
              1 1 0
              1 1 1
              2 1 0
              2 1 1
              0 0 0
              0 0 1
              1 0 0
              1 0 1
              2 0 0
              2 0 1
             ]*100;
 %}
 
 points_wall=[ 0 1 0
              0 1 1
              1 1 0
              1 1 1
              2 1 -0.5
              2 1 1.5
              0 0 0
              0 0 1
              1 0 0
              1 0 1
              2 0 -0.5
              2 0 1.5
             ]*100;
         
cell_wall=[
           8 0 1 3 2 6 7 9 8
           8 2 3 5 4 8 9 11 10
           ];
       
Nw=[
     0    -1     0
     0    -1     0
     0     1     0
     0     1     0
     1     0     0
    -1     0     0
     0     0     1
     0     0     1
     0     0    -1
     0     0    -1
     1     0     0
    -1     0     0
    ];

[~,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_mesh(points_wall,cell_wall);
N_points_wall=size(points_wall,1);
N_cell_wall=size(cell_wall,1);

 
 