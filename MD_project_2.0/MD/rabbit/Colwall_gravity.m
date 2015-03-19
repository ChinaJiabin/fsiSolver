%--------------------------------------------------------------------------
N_no_empty=Nw_cell(pos_cell(k),1);
id_w=Nw_cell(pos_cell(k),2:end)';

%--------------------------------------------
%For the case cells have different face number
id_w=id_w(id_w~=0);   
%---------------------------------------------

N_wall=length(id_w);

%--------------------------------------------------------------------------
%a:
  %a=0.5*sum(repmat(g,N_wall,1).*Nw(id_w,:),2);
   a=0.5*g*Nw(id_w,2);
%--------------------------------------------------------------------------
%b:
  b=sum(repmat(vel(k,:),N_wall,1).*Nw(id_w,:),2);
%--------------------------------------------------------------------------
%c:
  c=sum( ( Pw(id_w,:)-repmat(pos(k,:),N_wall,1) ).*Nw(id_w,:) ,2 );
  d_c=zeros(N_wall,1);
  d_c(1:N_no_empty)=-sign( c(1:N_no_empty) )*radius(k);
  c=-(c+d_c);
 
%--------------------------------------------------------------------------
%Search for collision event
%Precision control for c and b use same standard
id_1=logical( ( abs(c)<eps_colwall ).* ( abs(b)>eps_colwall ).*( a<0 ) );
delta_t1=max( 0,-b(id_1)./a(id_1) );

id_2=logical( ( abs(c)<eps_colwall ).* ( b<-eps_colwall ).*( a>=0 ) );
delta_t2=zeros( sum(id_2),1 );
                                                                  
id_3=logical( ( abs(c)>=eps_colwall ).*( a==0 ) );
delta_t3=-c(id_3)./b(id_3);

id_4=logical( (abs(c)>=eps_colwall ).*( a~=0 ));
delta_t4=( -b(id_4)+sqrt( b(id_4).^2-4*a(id_4).*c(id_4) ) )./( 2*a(id_4) );
delta_t5=( -b(id_4)-sqrt( b(id_4).^2-4*a(id_4).*c(id_4) ) )./( 2*a(id_4) );

delta_t=[delta_t1;delta_t2;delta_t3;delta_t4;delta_t5];
id_w_=[id_w(id_1);id_w(id_2);id_w(id_3);id_w(id_4);id_w(id_4)];

id=logical( (imag(delta_t)==0).*(delta_t>=0).*(delta_t~=Inf) );
N_add=sum(id);

%--------------------------------------------------------------------------
if N_add>0
    
  queue(count+1:count+N_add,:)=[delta_t(id),k*ones(N_add,1),-id_w_(id)];
  count=count+N_add;
  
end
  
 
  
