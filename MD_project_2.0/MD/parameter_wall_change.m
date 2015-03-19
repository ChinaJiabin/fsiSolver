function [Nw,Pw,Nw_cell,N_empty_wall, Nw_empty]=parameter_wall_change(Nw,Pw,Nw_cell,N_empty_wall, Nw_empty,id)
 
 %------------------将出口转化成可穿越的墙----------------------------------
 %           Nw:    出口面的法向量
 %           Pw：   出口面上任意一点
 %      Nw_cell:    组成的空间六面体所对应的六个面的标号矩阵，
 %                  其中每行的第一个数为不可穿越面的个数
 %,N_empty_wall：   不可穿越面的个数+1
 %     Nw_empty:    可穿越面所对应的两个体
 %           %P:    出口面上不同于Pw的任意一点
 %           id:    需要改变wall属性的wall的编号
%%-------------------------------------------------------------------------
 N=size(Nw,1);                         %所有面的总个数
%PPw=Pw-kron(ones(N,1),P);             %出口面上的一个向量
%id=find(sum(PPw.*Nw,2)==0);           %找出出口面所在行的行号

%--------------------------------------------------------------------------
%把不可穿越的墙转化成可穿越的墙
if id<N_empty_wall
    
   Nw=[Nw(1:id-1,:);Nw(id+1:end,:);Nw(id,:)];       %将出口面的法向量移到最后
   Pw=[Pw(1:id-1,:);Pw(id+1:end,:);Pw(id,:)];       %将出口面上任意一点移到最后
  
   Nw_cell_=Nw_cell(:,2:end);
   Nw_cell_=Nw_cell_- id*(Nw_cell_==id);            %将出口面的行号转化成0
   Nw_cell_=Nw_cell_- (Nw_cell_>id);                %将大于id的行号减1
   Nw_cell_=Nw_cell_+ N*(Nw_cell_==0);              %将等于0的行号转成最大行号
  
   N_empty_wall=N_empty_wall-1;                     %最大可穿越面行号减1
  
   Nw_cell=[sum(Nw_cell_<N_empty_wall,2),Nw_cell_]; %加上第一列不可穿越面的个数
  
   Nw_empty(:,1)=Nw_empty(:,1)-1;                   %可穿越面减1
   Np_cell=find( sum(Nw_cell_==N,2) );              %找到出口面所在行号
  
   if length(Np_cell)==1
      Nw_empty=[Nw_empty;[N Np_cell 0]];            %在Nw_empty列表最后加上出口面
   else
       Nw_empty=[Nw_empty;[N,Np_cell']];
   end
  
end
%--------------------------------------------------------------------------