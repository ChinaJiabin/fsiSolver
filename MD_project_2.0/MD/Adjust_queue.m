%--------------------------------------------------------------------------
queue(id_min,:)=[];                          %删除要发生的事件
count=count-1;
%--------------------------------------------------------------------------
if mark_j>0                                            %颗粒之间碰撞
    
   id=queue(1:count,2:3)==mark_i;
   id=sum(id,2)~=0;
   queue(id,:)=[];
   count=count-sum(id);
    
   id=queue(1:count,2:3)==mark_j;
   id=sum(id,2)~=0;
   queue(id,:)=[];
   count=count-sum(id);

else
     if  ~(-mark_j>=N_empty_wall)                     %颗粒与真实的墙碰撞
         
          id=queue(1:count,2:3)==mark_i;
          id=sum(id,2)~=0;
          queue(id,:)=[];
          count=count-sum(id);
          
     else
         
          id1=queue(1:count,2)==mark_i;               %颗粒穿越可穿越的墙但还在计算区域中运动
          id2=queue(1:count,3)<0;
          id=logical(id1.*id2);
          queue(id,:)=[];
          count=count-sum(id);
          
     end
end


%--------------------------------------------------------------------------
%未来事件的时间调整
queue(1:count,1)=queue(1:count,1)-timestep;
%--------------------------------------------------------------------------
