%--------------------------------------------------------------------------
%Collision bewteen particles and real wall
if   -mark_j==2
     position(mark_i,2)=position(mark_i,2)+high_wall-2*Radius;
     
elseif    -mark_j<N_empty_wall
    
         vel(mark_i,:)=vel(mark_i,:)-                                       ...
             (1+e_wall)*sum(vel(mark_i,:).*Nw(-mark_j,:))*Nw(-mark_j,:);
   
%{         
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
      
       
       N=N-1;
       continue;
      %-------------------------------------------------------------------- 
    end
  
%}
end
