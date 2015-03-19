%--------------------------------------------------------------------------
%Collision bewteen two particles considering the effect of rotation
%--------------------------------------------------------------------------
%Normal vector
delta_pos=pos(mark_i,:)-pos(mark_j,:); %Vector j points to i
vec_n=delta_pos/norm(delta_pos);    

%--------------------------------------------------------------------------
%Relative velocity
rel_vel_n= dot( vel(mark_j,:)-vel(mark_i,:),vec_n )*vec_n;
rel_vel_t= vel(mark_j,:)-vel(mark_i,:)-rel_vel_n+                       ...
           radius(mark_i)*cross( vel_ang(mark_i,:),vec_n )+             ...
           radius(mark_j)*cross( vel_ang(mark_j,:),vec_n );

%--------------------------------------------------------------------------
if ~isequal([0 0 0],rel_vel_t)      
   %Tangent vector
   vec_t=rel_vel_t/norm(rel_vel_t);          

   %-----------------------------------------------------------------------
   %Components of impulse
   J_n=(1+e_particle)*( mass(mark_i)*mass(mark_j)/( mass(mark_i)+mass(mark_j) ) )*rel_vel_n;   ...

   J_t=min(                                                                                    ...
           mu_particle*norm(J_n),                                                              ...
           2/7*mass(mark_i)*mass(mark_j)/( mass(mark_i)+ mass(mark_j) )*norm(rel_vel_t)        ...
           )*vec_t;

   J=J_n+J_t;
   
   %-----------------------------------------------------------------------
   %Update velocity and angle velocity according to impulse vector J
   vel(mark_i,:)=vel(mark_i,:)+J/mass(mark_i);
   vel(mark_j,:)=vel(mark_j,:)-J/mass(mark_j);

   vel_ang(mark_i,:)=vel_ang(mark_i,:)+5/( 2*mass(mark_i)*radius(mark_i) )*cross(J_t,vec_n);
   vel_ang(mark_j,:)=vel_ang(mark_j,:)+5/( 2*mass(mark_j)*radius(mark_j) )*cross(J_t,vec_n);
  
else%----------------------------------------------------------------------
   %Central collision
   J=(1+e_particle)*( mass(mark_i)*mass(mark_j)/( mass(mark_i)+mass(mark_j) ) )*rel_vel_n;
   vel(mark_i,:)=vel(mark_i,:)+J/mass(mark_i);
   vel(mark_j,:)=vel(mark_i,:)-J/mass(mark_j);
end
  %------------------------------------------------------------------------

