%--------------------------------------------------------------------------
%Collision bewteen particles and real wall 
%considering the effect of rotation
if  -mark_j<N_empty_wall
    
    vec_n=Nw(-mark_j,:);
    
    rel_vel_n=dot( -vel(mark_i,:),vec_n )*vec_n;
    rel_vel_t=-vel(mark_i,:)-rel_vel_n+radius(mark_i)*cross( vel_ang(mark_i,:),vec_n );
    
    if ~isequal([0 0 0],rel_vel_t) % norm(rel_vel_t)<1e-10
        
        vec_t=rel_vel_t/norm(rel_vel_t);          
        J_n=(1+e_wall)*mass(mark_i)* rel_vel_n; 
        J_t=min( mu_wall*norm(J_n),2/7*mass(mark_i)*norm(rel_vel_t) )*vec_t;    
        J=J_n+J_t;                                        
    
        vel(mark_i,:)=vel(mark_i,:)+J/mass(mark_i);
        vel_ang(mark_i,:)=vel_ang(mark_i,:)+5/( 2*mass(mark_i)*radius(mark_i) )*cross(J_t,vec_n);
        
    else
        J=(1+e_wall)*mass(mark_i)* rel_vel_n; 
        vel(mark_i,:)=vel(mark_i,:)+J/mass(mark_i);
    end
   
     
         
else
%--------------------------------------------------------------------------
%Collision bewteen particles and virtual wall.
     id=1-mark_j-N_empty_wall;
     
     if  pos_cell(mark_i)==Nw_empty(id,2)
         pos_cell(mark_i)=Nw_empty(id,3);
     else
         pos_cell(mark_i)=Nw_empty(id,2);
     end
     
    
    if pos_cell(mark_i)==0
        
       pos(mark_i,:)=[];
       pos_cell(mark_i)=[];
       vel(mark_i,:)=[];
       vel_ang(mark_i,:)=[];
       radius(mark_i,:)=[];
       mass(mark_i,:)=[];
       
      %--------------------------------------------------------------------
       %Adjust queue for the case that particle moves out of computing domain
       id=queue(1:count,2:3)==mark_i;
       id=sum(id,2)~=0;
       queue(id,:)=[];
       count=count-sum(id);
       
       queue(1:count,2:3)=queue(1:count,2:3)-(queue(1:count,2:3)>mark_i);
      
       %-------------------------------------------------------------------
       N=N-1;
       continue;
       
    end
  

end