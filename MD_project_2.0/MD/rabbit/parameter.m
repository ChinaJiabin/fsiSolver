%Time Parameter
cpu_time=cputime;
time=0;
time_end=0.7;

%Physcial coefficient Parameter 
e_wall=1;                                 %Coefficient of restitution with wall 
e_particle=0.9;                           %Coefficient of restitution with particles
mu_wall=0.08;                             %Coefficient of friction with wall
mu_particle=0.08;                         %oefficient of friction with particles
g=-9.8e3;                                 %Gravity 

%Statistics Parameter
N_col_particles=0;

time_serial=zeros(10e3,1);
nd_serial=zeros(10e3,1);
rel_vel_serial=zeros(10e3,1);
mean_vel_serial=zeros(10e3,1);
mm_vel_serial=zeros(10e3,1);

N_Statistics_window=11;                  %The serial number of the statistics window             
%IO Parameter
case_name=[];
file_path=case_name;
file_write_time=0.01;
file_count=0;                             %The maximum file number is 9999
loop_count=0;

%Queue Parameter
queue=zeros(1e4,3);
count=0;                                  %future event number

%floating point precision parameter
eps_colwall=1e-11;

%--------------------------------------------------------------------------
%{%
delete('vtk/*.vtk');
delete('picture/*.png');
%}
out_vtk_wall;
%--------------------------------------------------------------------------
      
    
     
