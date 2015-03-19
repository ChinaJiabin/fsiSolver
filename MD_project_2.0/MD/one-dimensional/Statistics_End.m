vel_mean=vel(:,2)-mean( vel(:,2) );
hist( vel_mean , min(vel_mean)-.5:6:max(vel_mean)+.5 );

%
%   collision rate=  loop_count 
%   number density=  N
%   particle radius= radius
%   The speed of statistics:
%                           mean_vel