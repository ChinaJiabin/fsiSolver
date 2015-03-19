if mark_j>0
    
  if pos_cell(mark_i)==N_Statistics_window && pos_cell(mark_j)==N_Statistics_window
      
     N_col_particles=N_col_particles+1;
     id=pos_cell==N_Statistics_window;
     
     %Collision time
     time_serial(N_col_particles)=time;
     
     %Number density
     nd_serial(N_col_particles)=sum(id); 
     
     %Relative velocity
     rel_vel_serial(N_col_particles)=sta_vel_rel( vel(id,:) )/1000;
     
     %Mean velocity
     mean_vel_serial(N_col_particles)=mean( sqrt( sum( vel(id,:).^2,2 ) ) );
     
     %Modify mean velocity
     vel_mod=vel(id,:);
     vel_mod(:,2)=vel_mod(:,2)-mean( vel_mod(:,2) );
     mm_vel_serial(N_col_particles)=mean( sqrt( sum( vel_mod.^2,2 ) ) );
     
  end
  
end
     
