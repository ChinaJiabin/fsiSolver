delta_pos=pos(mark_j,:)-pos(mark_i,:);
delta_vel=vel(mark_j,:)-vel(mark_i,:);
tau=radius(mark_i)+radius(mark_j);

J=(1+e_particle)*mass(mark_i)*mass(mark_j)*(sum(delta_pos.*delta_vel))/ ...
 (tau*(mass(mark_i)+mass(mark_j)));

vel(mark_i,:)=vel(mark_i,:)+J*delta_pos/(tau*mass(mark_i));
vel(mark_j,:)=vel(mark_i,:)-J*delta_pos/(tau*mass(mark_j));

 

