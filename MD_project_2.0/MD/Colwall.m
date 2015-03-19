%--------------------------------------------------------------------------
N_no_empty=Nw_cell(pos_cell(k),1);
id_w=Nw_cell(pos_cell(k),2:end)';

%--------------------------------------------
%For the case cells have different face number
id_w=id_w(id_w~=0);   
%---------------------------------------------

N_wall=length(id_w);
%--------------------------------------------------------------------------
dis_p_to_w=sum((Pw(id_w,:)-repmat(pos(k,:),N_wall,1)).*Nw(id_w,:),2);

d_dis_p_to_w=zeros(N_wall,1);
d_dis_p_to_w(1:N_no_empty)=-sign( dis_p_to_w(1:N_no_empty) )*radius(k);
dis_p_to_w=dis_p_to_w+d_dis_p_to_w;
 
%-------------------------------------------------------------------------- 
vel_p_to_w=sum(repmat(vel(k,:),N_wall,1).*Nw(id_w,:),2);
%--------------------------------------------------------------------------
id_1=logical( ( abs(dis_p_to_w)<eps_colwall ) .*( vel_p_to_w<0 ) );
delta_t=zeros(sum(id_1),1);

id_2=abs(dis_p_to_w)>=eps_colwall;
delta_t=[delta_t;dis_p_to_w(id_2) ./vel_p_to_w(id_2)];

id_w_=[id_w(id_1);id_w(id_2)];

id=logical( (delta_t>=0).*(delta_t~=Inf) );
N_add=sum(id);
%--------------------------------------------------------------------------

if N_add>0
    
  queue(count+1:count+N_add,:)=[delta_t(id),k*ones(N_add,1),-id_w_(id)];
  count=count+N_add;
  
end
%--------------------------------------------------------------------------