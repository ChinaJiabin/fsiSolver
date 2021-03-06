%Time Parameter
cpu_time=cputime;
time=0;
time_end=100;

%Physcial coefficient Parameter
e_wall=1;                                     %Coefficient of restitution with wall 
e_particle=1;                                 %Coefficient of restitution with particles
g=0;                                          %Gravity 

%Statistics Parameter
statistics=zeros(N,3);
system_kinetic_energy0=sum(.5*mass.*sum(vel.^2,2)); 
average_molecular_momentum0=sum(mass.*sum(vel,2))/N; 

%IO Parameter
case_name=[];
file_path=[];
file_write_time=0.2;
file_count=0;                             %The maximum file number is 9999
loop_count=0;

%Queue Parameter
queue=zeros(1e4,3);
count=0;                                  %future event number


%floating point precision parameter
eps_colwall=1e-12;

%--------------------------------------------------------------------------
delete('vtk/*.vtk');
delete('picture/*.png');
out_vtk_wall;
%--------------------------------------------------------------------------
      
    
     
