function pos_cell=parameter_posCell(pos,Nw,Pw,Nw_cell)
%ȷ���������ڵ�Ԫ���

N=size(pos,1);                                      %��������
N_cell=size(Nw_cell,1);                             %��Ԫ����

pos_cell=zeros(N,1);

for i=1:N                                            %�������п���
    
    for j=1:N_cell                                   %�������е�Ԫ
        
        Nw_=Nw(Nw_cell(j,2:end),:);                  % Nw_��һ����Ԫ�����з�����
        Pw_=Pw(Nw_cell(j,2:end),:);                  % Pw_��һ����Ԫ�������ϵ�����һ��
        
        if ( sum ( sum ( Nw_.*(  Pw_- repmat(pos(i,:),6,1)  ), 2 )>0 )==0  )                    
            pos_cell(i)=j;
            break;
            
        end
    end
end
