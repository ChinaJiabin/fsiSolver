[timestep,id_min]=min(queue(1:count,1));
mark_i=queue(id_min,2);
mark_j=queue(id_min,3);

pos= pos+timestep*vel;
pos(:,2)= pos(:,2)+0.5*g*timestep^2;
vel(:,2)= vel(:,2)+g*timestep;

time=time+timestep;
