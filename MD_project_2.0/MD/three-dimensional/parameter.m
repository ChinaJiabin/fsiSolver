%Time Parameter
cpu_time=cputime;
time=0;
time_end=50; 
time_add=0.2;                                  %The time interval for adding particles

%Physcial coefficient Parameter
e_wall=1;                                       %Coefficient of restitution with wall 
e_particle=1;                                   %Coefficient of restitution with particles
mu_wall=0.1;                                    %Coefficient of friction with wall
mu_particle=0.1;                                %oefficient of friction with particles
g=-9.8;                                         %Gravity 

%Statistics Parameter
statistics=zeros(N,3);
system_kinetic_energy0=sum(.5*mass.*sum(vel.^2,2)); 
average_molecular_momentum0=sum(mass.*sum(vel,2))/N; 

%IO Parameter
case_name=[];
file_path=[];
file_write_time=0.1;
file_count=0;                             %The maximum file number is 9999
loop_count=0;

%Queue Parameter
queue=zeros(1e4,3);
count=0;                                  %future event number

%floating point precision parameter
eps_colwall=1e-10;

%--------------------------------------------------------------------------
delete('vtk/*.vtk');
delete('picture/*.png');
out_vtk_wall;
%--------------------------------------------------------------------------
      
    
     
