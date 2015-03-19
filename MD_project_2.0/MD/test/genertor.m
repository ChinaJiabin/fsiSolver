fprintf('initialization by genertor_special\n\n\n')
                                                     %Particle postion
%{ 
pos=[ 
          kron(ones(3,1),(25:25:175)')   ,    ...
          kron((25:2:29)',ones(7,1))     ,   ...
          kron(50*ones(3,1),ones(7,1))
     ];
%} 
                                                     
pos=[
    100 50 50
    150 50 50
    ];
                                                    
                                                         %Wall cell that particles is in
pos_cell=parameter_posCell(pos,Nw,Pw,Nw_cell);

N=size(pos,1);                                           %Particle number   

vel=[                                                    %Particle velocity
       0 0 0                             
     -20 0 0
      ];
vel_ang=kron(ones(N,1),[0 0 0]);
mass=ones(N,1);                                          %Particle mass
   
radius=ones(N,1);                                        %Particle radius
         
   
    