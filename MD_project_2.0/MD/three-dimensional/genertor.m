%--------------------------------------------------------------------------
%{%
fprintf('initialization by genertor_special\n\n\n')
                                                          %Particle postion    
x_init=60:10:340;
N_x_init=length(x_init);

y_init=h1+h2+sqrt(3)*(l2-l1)/2-100;

z_init=50:10:100;
N_z_init=length(z_init);

pos_init=[
          kron(ones(N_z_init,1),x_init'),         ...
          y_init*ones(N_x_init*N_z_init,1),  ...
          kron(z_init',ones(N_x_init,1))
          ];                                               %A layer of particles
                                                    
                                                           %Wall cell that particles is in
pos_cell_init=parameter_posCell(pos_init,Nw,Pw,Nw_cell); 

N_init=length(pos_cell_init);                               %Particle number  

vel_init=zeros(N_init,3);                                   %Particle velocity

vel_ang_init=zeros(N_init,3);                               %Particle angle velocity

mass_init=ones(N_init,1);                                   %Particle mass
   
radius_init=1.5*ones(N_init,1);                             %Particle radius

pos=pos_init;
pos_cell=pos_cell_init;
vel=vel_init;
vel_ang=vel_ang_init;
mass=mass_init;
radius=radius_init;
N=length(pos_cell); 
  %}
%------------------------------------

%{
%For test
pos=[
    kron(ones(10,1),linspace(100,300,8)'),                                  ...
    h1+h2+sqrt(3)*(l2-l1)/2-kron(linspace(100,200,10)',ones(8,1))    ...
    6.5*ones(10*8,1)                                                 ...
    ];
pos=pos-rand( size(pos) );
%}
%{
pos=[
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-100 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-100 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-200 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-200 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-300 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-300 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-400 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-400 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-150 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-150 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-250 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-250 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-350 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-350 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-125 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-125 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-225 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-225 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-325 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-325 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-175 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-175 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-275 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-275 l3/2
    450/2 h1+h2+sqrt(3)*(l2-l1)/2-375 l3/2
    100/2 h1+h2+sqrt(3)*(l2-l1)/2-375 l3/2
    ];
%}
                                                     
                                                            %Wall cell that particles is in
pos_cell=parameter_posCell(pos,Nw,Pw,Nw_cell); 

N=length(pos_cell);                                          %Particle number  

vel=zeros(N,3);                                              %Particle velocity
     
mass=ones(N,1);                                              %Particle mass
   
radius=ones(N,1);                                            %Particle radius


%} 
%{
%--------------------------------------------------------------------------
%For cube
pos_init=[
          50 80 50
          ];                                               %A layer of particles
                                                    
                                                           %Wall cell that particles is in
pos_cell_init=parameter_posCell(pos_init,Nw,Pw,Nw_cell); 

N_init=length(pos_cell_init);                               %Particle number  

vel_init=kron(ones(N_init,1),[0 0 0]);                     %Particle velocity
     
mass_init=ones(N_init,1);                                   %Particle mass
   
radius_init=ones(N_init,1);                                 %Particle radius

  pos=pos_init;
  pos_cell=pos_cell_init;
  vel=vel_init;
  mass=mass_init;
  radius=radius_init;
  N=length(pos_cell); 

%--------------------------------------------------------------------------
%}