%--------------------------------------------------------------------------
queue(id_min,:)=[];                          %ɾ��Ҫ�������¼�
count=count-1;
%--------------------------------------------------------------------------
if mark_j>0                                            %����֮����ײ
    
   id=queue(1:count,2:3)==mark_i;
   id=sum(id,2)~=0;
   queue(id,:)=[];
   count=count-sum(id);
    
   id=queue(1:count,2:3)==mark_j;
   id=sum(id,2)~=0;
   queue(id,:)=[];
   count=count-sum(id);

else
     if  ~(-mark_j>=N_empty_wall)                     %��������ʵ��ǽ��ײ
         
          id=queue(1:count,2:3)==mark_i;
          id=sum(id,2)~=0;
          queue(id,:)=[];
          count=count-sum(id);
          
     else
         
          id1=queue(1:count,2)==mark_i;               %������Խ�ɴ�Խ��ǽ�����ڼ����������˶�
          id2=queue(1:count,3)<0;
          id=logical(id1.*id2);
          queue(id,:)=[];
          count=count-sum(id);
          
     end
end


%--------------------------------------------------------------------------
%δ���¼���ʱ�����
queue(1:count,1)=queue(1:count,1)-timestep;
%--------------------------------------------------------------------------
