%--------------------------------------------------------------------------
[timestep,id_min]=min(queue(1:count,1));
mark_i=queue(id_min,2);
mark_j=queue(id_min,3);

temp_time=timestep;
remain=file_write_time-mod(time,file_write_time);

%--------------------------
%variable used to break
flag=0;
%--------------------------

while 1
    %{
      %Code for adding particles dynamically
     
       if  ( mod(time,time_add)<1e-10 || mod(time,time_add)>time_add-1e-10 ) && time 
        
           pos=[pos;pos_init];
           pos_cell=[pos_cell;pos_cell_init];
           vel=[vel;vel_init];
           mass=[mass;mass_init];
           radius=[radius;radius_init];
             
           %---------------------------------------------------------
           %Adjust the queue of future event for new adding particles
           count_temp=count;
        
           for k=N+1:N+N_init
               Colwall_gravity;
           end
         %{
           for i=N+1:N+N_init
               for j=1:i-1
                   Colparticles;
               end
           end
         %}
           N=N+N_init;
        
          if min ( queue(count_temp+1:count,1) )< temp_time;
             flag=1;
             break;
         else
             queue(count_temp+1:count,1)=queue(count_temp+1:count,1)+timestep-temp_time; 
          end
         %----------------------------------------------------------
       end
      %}
      if  remain<temp_time
          
          pos= pos+remain*vel;
          pos(:,2)= pos(:,2)+0.5*g*remain^2;
          vel(:,2)= vel(:,2)+g*remain;
      
          out_files;
      
          time=time+remain;
          temp_time=temp_time-remain;
          remain=file_write_time-mod(time,file_write_time);
      else
          break;
      end
end
%
if flag
   continue;
end

pos= pos+temp_time*vel;
pos(:,2)= pos(:,2)+0.5*g*temp_time^2;
vel(:,2)= vel(:,2)+g*temp_time;

time=time+temp_time;
%--------------------------------------------------------------------------