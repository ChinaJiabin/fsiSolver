fid=fopen([file_path,'vtk/wall.vtk'],'w');
%--------------------------------------------------------------------------
%Header
fprintf(fid,'%s\n','# vtk DataFile Version 3.1 ');
fprintf(fid,'%s\n','Visualization for wall');
fprintf(fid,'%s\n','ASCII');
fprintf(fid,'%s\n','DATASET UNSTRUCTURED_GRID');
%--------------------------------------------------------------------------
%Mesh information
fprintf(fid,'\n%s\n',['POINTS ',num2str(N_points_wall),' float']);
fprintf(fid,'%f    %f    %f\n',points_wall');

fprintf(fid,'\n%s\n',['CELLS ',num2str(N_cell_wall),' ',num2str(9*N_cell_wall)]);
fprintf(fid,'%d  %d  %d  %d  %d  %d  %d  %d  %d \n',cell_wall');

fprintf(fid,'\n%s\n',['CELL_TYPES ',num2str(N_cell_wall)]);
fprintf(fid,'%d ',12*ones(N_cell_wall,1));

%--------------------------------------------------------------------------
fclose(fid);