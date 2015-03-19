fid=fopen([file_path,'vtk/particle_', file_str_count,'.vtk'],'w');
%--------------------------------------------------------------------------
%Header
fprintf(fid,'%s\n','# vtk DataFile Version 3.1 ');
fprintf(fid,'%s\n','Visualization for particles movement');
fprintf(fid,'%s\n','ASCII');
fprintf(fid,'%s\n','DATASET UNSTRUCTURED_GRID');

%--------------------------------------------------------------------------
%Mesh information
fprintf(fid,'\n%s\n',['POINTS ',num2str(N),' float']);
fprintf(fid,'%f    %f    %f\n',pos');

fprintf(fid,'\n%s\n',['CELLS ',num2str(N),' ',num2str(2*N)]);
fprintf(fid,'%d    %d \n',[ones(N,1),(0:N-1)']');

fprintf(fid,'\n%s\n',['CELL_TYPES ',num2str(N)]);
fprintf(fid,'%d ',ones(N,1));

%--------------------------------------------------------------------------
%Point information
fprintf(fid,'\n\n%s\n\n',['POINT_DATA ',num2str(N)]);

 %Velocity magnitude
 fprintf(fid,'\n%s\n',['SCALARS ','vel_mag', ' float']);
 fprintf(fid,'%s\n','LOOKUP_TABLE default');
 fprintf(fid,'%f\n',sum(vel.^2,2)');
 fprintf(fid,'\n');

 %Angle velocity magnitude
 fprintf(fid,'\n%s\n',['SCALARS ','vel_ang_mag', ' float']);
 fprintf(fid,'%s\n','LOOKUP_TABLE default');
 fprintf(fid,'%f\n',sum(vel_ang.^2,2)');
 fprintf(fid,'\n');

 %Velocity
 fprintf(fid,'\n%s\n',['VECTORS ','velocity', ' float']);
 fprintf(fid,'%f  %f  %f\n',vel');
 fprintf(fid,'\n');
 
 %Angle velocity
 fprintf(fid,'\n%s\n',['VECTORS ','angle_velocity', ' float']);
 fprintf(fid,'%f  %f  %f\n',vel_ang');
 fprintf(fid,'\n');
 
%--------------------------------------------------------------------------
fclose(fid);

