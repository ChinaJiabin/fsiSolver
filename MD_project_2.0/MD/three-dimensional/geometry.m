%Geometry Parameter
 %-------------------------------------------------------------------------

l1=185;
l2=398;
l3=144;
h1=500;
h2=600;

points_wall=[
             (l2-l1)/2,0,0
             (l2-l1)/2,l3,0
             (l1+l2)/2,0,0
             (l1+l2)/2,l3,0
             (l2-l1)/2,0,h1
             (l2-l1)/2,l3,h1
             (l1+l2)/2,0,h1
             (l1+l2)/2,l3,h1
             0,0,h1+sqrt(3)*(l2-l1)/2
             0,l3,h1+sqrt(3)*(l2-l1)/2
             l2,0,h1+sqrt(3)*(l2-l1)/2
             l2,l3,h1+sqrt(3)*(l2-l1)/2
             0,0,h1+h2+sqrt(3)*(l2-l1)/2
             0,l3,h1+h2+sqrt(3)*(l2-l1)/2
             l2,0,h1+h2+sqrt(3)*(l2-l1)/2
             l2,l3,h1+h2+sqrt(3)*(l2-l1)/2
            ];

points_wall=[points_wall(:,1),points_wall(:,3),points_wall(:,2)];

cell_wall=[
           8 4 5 7 6 0 1 3 2
           8 8 9 11 10 4 5 7 6
           8 12 13 15 14 8 9 11 10
           ];
       
[Nw,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_mesh(points_wall,cell_wall);
[Nw,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_wall_change(Nw,Pw,Nw_cell,N_empty_wall, Nw_empty,2);
 N_points_wall=size(points_wall,1);
 N_cell_wall=size(cell_wall,1);

 
 