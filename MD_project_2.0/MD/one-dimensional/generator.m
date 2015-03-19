fprintf('initialization by genertor_special\n\n\n')
                                                         %Particle postion 
%{    
N_init=1;                                                   
Radius=1;
d_sphere=3*Radius;

id=randperm ( floor( high_wall/(2*Radius+d_sphere) ) )';
pos_y=(2*Radius+d_sphere)*id(1:N_init)  ...
      -(Radius+d_sphere/2);
  
pos_y=sort(pos_y);  
N=length(pos_y);                                         %Particle number
pos=[5*ones(N,1),pos_y,5*ones(N,1)];
%} 
                                                         
%{%                                                 
pos=[
    5 50 5
    5 25 5
    ];
Radius=2;
N=size(pos,1);
%}                                                         
                                                          %Wall cell that particles is in
pos_cell=ones(N,1);

   
 
                                                          %Particle velocity
vel=[
     0  0  0
     0 -10 0
     ];
vel_ang=zeros(2,3);

                                                          %Particle mass
mass=[
      Inf
      1
      ];
   
                                                          %Particle radius
 radius=[
          1
          1
         ];
         
   
    