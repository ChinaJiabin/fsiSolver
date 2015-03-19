fprintf('initialization by generator\n\n\n')
%-----------------------------------------
%Particle number
 N=2*N_l_init*N_w_init;
 
%-----------------------------------------

origin_point_1=(width/2- pole_distance/2 - pole_width/sin(pole_angle) - (pole_length-l_init)*cos(pole_angle)) ...
                +1i*(height+(pole_length-l_init)*sin(pole_angle));
            
origin_point_2=(width/2+ pole_distance/2 + pole_width/sin(pole_angle)+ (pole_length-l_init)*cos(pole_angle)) ...
                 +1i*(height+(pole_length-l_init)*sin(pole_angle));
          
[x_init,y_init]=meshgrid(                                               ...
                         linspace(0,w_init,N_w_init+1),                 ...
                         linspace(0,l_init,N_l_init+1)                  ...
                         );
                     
x_yi_init= reshape(x_init+1i*y_init,[],1)-                              ...
           (w_init/(2*N_w_init)+1i*l_init/(2*N_l_init));
       
x_yi_init=x_yi_init(real(x_yi_init)>0);
x_yi_init=x_yi_init(imag(x_yi_init)>0);

x_yi_init_1=x_yi_init*exp( 1i*pi/6)+origin_point_1;
x_yi_init_2=(x_yi_init-pole_width)*exp(-1i*pi/6)+origin_point_2;

%---------------------------------------------
%Particle postion
pos=[
      real([x_yi_init_1;x_yi_init_2]),    ...
      imag([x_yi_init_1;x_yi_init_2]),    ...            
      1.75*ones(N,1)
     ];
%---------------------------------------------
%Wall cell that particles is in

pos_cell=parameter_posCell(pos,Nw,Pw,Nw_cell);
     %Modify pos and pos_cell
     id=pos_cell~=0;
     pos_cell=pos_cell(id);
     pos=pos(id,:);
     N=length(pos_cell);

%---------------------------------------------  
%Particle velocity
vel=0*rand(N,3);
vel_ang=0*rand(N,3);
%---------------------------------------------
%Particle mass
mass=ones(N,1);
%---------------------------------------------
%Particle radius
radius=0.5*ones(N,1);
%---------------------------------------------
 N_init=N;
