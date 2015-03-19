function [Nw,Pw,Nw_cell,N_empty_wall, Nw_empty,faces]=parameter_mesh(points,cells)
 %--------------------------------------------------------------------------
 %           Nw:    ��ķ�����
 %           Pw��   ��������һ��
 %      Nw_cell:    ��ɵĿռ�����������Ӧ��������ı�ž���
 %                  ����ÿ�еĵ�һ����Ϊ���ɴ�Խ��ĸ���
 %,N_empty_wall��   ���ɴ�Խ��ĸ���+1
 %     Nw_empty:    �ɴ�Խ������Ӧ��������
 %-------------------------------------------------------------------------
 %faces
 N_cell=size(cells,1);          % N_cell:�����嵥Ԫ�ĸ���
 cells_=cells(:,2:end)+1;       % cells_:
 
 id=[
     1 2 3 4;
     5 8 7 6;
     1 5 6 2;
     4 3 7 8;
     1 4 8 5;
     2 6 7 3;
     ];
 
 faces=zeros( 6*N_cell,4);
 for i=1:6
     faces((i-1)*N_cell+1:i*N_cell,:)=cells_(:,id(i,:));           %�������е���
 end
         
 faces_inv=faces(:,[1,4,3,2]);                                     %��ÿ������ĸ��㷴���ʾ
 [~,id_faces,id_faces_inv]=intersect(faces,faces_inv,'rows');      %id_faces_inv���غ��棨�ɴ�͸�棩�����
 
 faces=[faces,kron(ones(6,1),(1:N_cell)'),zeros(6*N_cell,1)];
 faces(id_faces,6)=mod(id_faces_inv,N_cell)+        ...
                  N_cell*(mod(id_faces_inv,N_cell)==0);
 faces=sortrows(faces,6);
 %-------------------------------------------------------------------------
 %Nw
 Nw=-cross(                                                       ...
         points(faces(:,2),:)-points(faces(:,1),:),               ...
         points(faces(:,3),:)-points(faces(:,1),:),               ...
         2                                                        ...
          );
      
for i=1:length(Nw)                    %Normalize vectors
    Nw(i,:)=Nw(i,:)/norm(Nw(i,:));
end
%--------------------------------------------------------------------------
%Pw
Pw= points(faces(:,1),:);
%--------------------------------------------------------------------------
%N_empty_wall
id_zeros=faces(:,6)==0;
N_empty_wall=sum(id_zeros)+1;
%--------------------------------------------------------------------------
%Nw_cell
Nw_cell=zeros(N_cell,7);

for i=1:N_cell
    id=faces(:,5)==i;
    Nw_cell(i,2:end)=find(id)';
    Nw_cell(i,1)=sum(id.*id_zeros);
end  
%--------------------------------------------------------------------------
%Nw_empty
 if N_empty_wall>length(faces)
    Nw_empty=[];
 else
    Nw_empty=[(N_empty_wall:length(faces))',faces(N_empty_wall:end,[5,6])];
 end
 %-------------------------------------------------------------------------