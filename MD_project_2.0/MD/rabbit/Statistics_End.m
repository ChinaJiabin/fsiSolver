
time_serial=time_serial(1:N_col_particles);
nd_serial=nd_serial(1:N_col_particles);
rel_vel_serial=rel_vel_serial(1:N_col_particles);
mean_vel_serial=mean_vel_serial(1:N_col_particles);
mm_vel_serial=mm_vel_serial(1:N_col_particles);
save(num2str( N_init),'time_serial','nd_serial','rel_vel_serial','mean_vel_serial','mm_vel_serial')
