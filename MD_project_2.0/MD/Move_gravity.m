[timestep,id_min]=min(queue(1:count,1));
mark_i=queue(id_min,2);
mark_j=queue(id_min,3);

temp_time=timestep;
remain=file_write_time-mod(time,file_write_time);

while remain<temp_time
   
      pos= pos+remain*vel;
      pos(:,2)= pos(:,2)+0.5*g*remain^2;
      vel(:,2)= vel(:,2)+g*remain;
      
      out_files;
      
      time=time+remain;
      temp_time=temp_time-remain;
      remain=file_write_time-mod(time,file_write_time);
    
end

pos= pos+temp_time*vel;
pos(:,2)= pos(:,2)+0.5*g*temp_time^2;
vel(:,2)= vel(:,2)+g*temp_time;

time=time+temp_time;
