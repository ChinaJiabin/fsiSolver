function [Nw,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_wall_change(Nw,Pw,Nw_cell,N_empty_wall, Nw_empty,id)
 
 %------------------������ת���ɿɴ�Խ��ǽ----------------------------------
 %           Nw:    ������ķ�����
 %           Pw��   ������������һ��
 %      Nw_cell:    ��ɵĿռ�����������Ӧ��������ı�ž���
 %                  ����ÿ�еĵ�һ����Ϊ���ɴ�Խ��ĸ���
 %,N_empty_wall��   ���ɴ�Խ��ĸ���+1
 %     Nw_empty:    �ɴ�Խ������Ӧ��������
 %           %P:    �������ϲ�ͬ��Pw������һ��
 %           id:    ��Ҫ�ı�wall���Ե�wall�ı��
%%-------------------------------------------------------------------------
 N=size(Nw,1);                         %��������ܸ���
%PPw=Pw-kron(ones(N,1),P);             %�������ϵ�һ������
%id=find(sum(PPw.*Nw,2)==0);           %�ҳ������������е��к�

%--------------------------------------------------------------------------
%�Ѳ��ɴ�Խ��ǽת���ɿɴ�Խ��ǽ
if id<N_empty_wall
    
   Nw=[Nw(1:id-1,:);Nw(id+1:end,:);Nw(id,:)];       %��������ķ������Ƶ����
   Pw=[Pw(1:id-1,:);Pw(id+1:end,:);Pw(id,:)];       %��������������һ���Ƶ����
  
   Nw_cell_=Nw_cell(:,2:end);
   Nw_cell_=Nw_cell_- id*(Nw_cell_==id);            %����������к�ת����0
   Nw_cell_=Nw_cell_- (Nw_cell_>id);                %������id���кż�1
   Nw_cell_=Nw_cell_+ N*(Nw_cell_==0);              %������0���к�ת������к�
  
   N_empty_wall=N_empty_wall-1;                     %���ɴ�Խ���кż�1
  
   Nw_cell=[sum(Nw_cell_<N_empty_wall,2),Nw_cell_]; %���ϵ�һ�в��ɴ�Խ��ĸ���
  
   Nw_empty(:,1)=Nw_empty(:,1)-1;                   %�ɴ�Խ���1
   Np_cell=find( sum(Nw_cell_==N,2) );              %�ҵ������������к�
  
   if length(Np_cell)==1
      Nw_empty=[Nw_empty;[N Np_cell 0]];            %��Nw_empty�б������ϳ�����
   else
       Nw_empty=[Nw_empty;[N,Np_cell']];
   end
  
end
%--------------------------------------------------------------------------