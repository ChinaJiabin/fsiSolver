%--------------------------------------------------------------------------
%Geometry Parameter
%一个立方体
points_wall=[
             0 0 0
             0 0 1
             1 0 0
             1 0 1
             0 1 0
             0 1 1
             1 1 0
             1 1 1
             ]*100;

cell_wall=[
           8 4 5 7 6 0 1 3 2
          ];

Nw=[
    0 -1 0
    1 0 0
    -1 0 0
    0 0 1
    0 0 -1
    0 1 0
   ];

Pw=[
    50 100 50
    0 50 50
    100 50 50
    50 50 0
    50 50 100
     50 0 50
   ];

Nw_cell=[
         5 1 2 3 4 5 6 
        ];

N_empty_wall=6;
Nw_empty=[6 1 0];

N_points_wall=8;
N_cell_wall=1;

%[Nw,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_wall_change(Nw,Pw,Nw_cell,N_empty_wall,Nw_empty,1);
%--------------------------------------------------------------------------


 