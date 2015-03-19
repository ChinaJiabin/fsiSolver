function pos_cell=parameter_posCell(pos,Nw,Pw,Nw_cell)
%确定颗粒所在单元编号

N=size(pos,1);                                      %颗粒数量
N_cell=size(Nw_cell,1);                             %单元数量

pos_cell=zeros(N,1);

for i=1:N                                            %遍历所有颗粒
    
    for j=1:N_cell                                   %遍历所有单元
        
        Nw_=Nw(Nw_cell(j,2:end),:);                  % Nw_：一个单元的所有法向量
        Pw_=Pw(Nw_cell(j,2:end),:);                  % Pw_：一个单元各个面上的任意一点
        
        if ( sum ( sum ( Nw_.*(  Pw_- repmat(pos(i,:),6,1)  ), 2 )>0 )==0  )                    
            pos_cell(i)=j;
            break;
            
        end
    end
end
