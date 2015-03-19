fprintf('initialization by genertor\n\n\n')
                                                         %Particle postion 
%{  
N_init;                                                   
Radius=0.01;
d_sphere=3*Radius;
%{
pos_y=(2*Radius+d_sphere)*                                               ...
      unique( ceil( rand(N_init,1)*high_wall/( (2*Radius+d_sphere)) ) )- ...
      (Radius+d_sphere/2);
%}
id=randperm ( floor( high_wall/(2*Radius+d_sphere) ) )';
pos_y=(2*Radius+d_sphere)*id(1:N_init)  ...
      -(Radius+d_sphere/2);
  
pos_y=sort(pos_y);  
N=length(pos_y);                                         %Particle number
pos=[5*ones(N,1),pos_y,5*ones(N,1)];
%} 
                                                         
%{ %                                                 
pos=[
    %{
    5 4  5
    5 10 5
    5 25 5
    5 35 5
    %}
    5 30 5
    5 50 5
    ];
Radius=2;
N=size(pos,1);
%}                                                         
                                                         %Wall cell that particles is in
pos_cell=ones(N,1);

   

vel=kron(ones(N,1),[0 0 0]);                             %Particle velocity
vel_ang=kron(ones(N,1),[0 0 1]);    
mass=ones(N,1);                                          %Particle mass
   
radius=Radius*ones(N,1);                                 %Particle radius
         
   
    