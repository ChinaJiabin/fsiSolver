[timestep,id_min]=min(queue(1:count,1));
mark_i=queue(id_min,2);
mark_j=queue(id_min,3);

temp_time=timestep;
remain=file_write_time-mod(time,file_write_time);

while remain<=temp_time
    
      pos= pos+remain*vel;
      time=time+remain;
     
      out_files;
     
      temp_time=temp_time-remain;
      remain=file_write_time-mod(time,file_write_time);
    
end

 pos= pos+temp_time*vel;
 time=time+temp_time;


    