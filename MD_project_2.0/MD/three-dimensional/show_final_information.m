fprintf('........................................................\n')
fprintf('Virtual time of simluation is %f\n',time)
fprintf('Time consuming of simluation is %f\n',cputime-cpu_time)
fprintf('........................................................\n')
fprintf('Number of loop in the simulation is %d\n',loop_count)
fprintf('Number of files for visualization  is %d\n',file_count)
fprintf('........................................................\n')
%{
fprintf('Flow rate is %f\n',1/time_add*2500*sum(4/3*pi*(radius_init/1000).^3))
%}

