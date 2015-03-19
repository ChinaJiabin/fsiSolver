if pos_cell(i)==pos_cell(j) %Determine particle i and j whether in the same domian
    
   delta_pos=pos(j,:)-pos(i,:)
   delta_vel=vel(j,:)-vel(i,:)
   delta_d=sum(delta_pos.*delta_vel)
       
  if delta_d<0   
 
     d=delta_d^2-norm(delta_vel)^2*(norm(delta_pos)^2-(radius(i)+radius(j))^2)
 
     if d>=0
        count=count+1;
        queue(count,:)=[-(delta_d+sqrt(d))/norm(delta_vel)^2,i,j];
     end
      
  end
  
end
