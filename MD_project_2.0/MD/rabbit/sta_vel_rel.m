function vel_rel=sta_vel_rel(vel)

N=size(vel,1); 
vel_rel=0;

for i=1:N-1
    
    for j=i+1:N
        
        vel_rel=vel_rel+norm(vel(i,:)-vel(j,:));
        
    end
end

vel_rel=2*vel_rel/( N*(N-1) );