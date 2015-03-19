%{%

data_fc=zeros(700,1);
data_n=zeros(700,1);
data_dia=zeros(700,1);
data_vel_rel=zeros(700,1);

data_raduis=(0.01:0.01:0.1)*100;
data_coeff=size( 1 , length(data_raduis) );
count_=0;

coeff=[];
for Raduis=0.01:0.01:0.1
    count=0;
     for   n=50:50:500
         
         if exist(['data/',num2str(n),'-',num2str(Raduis),'.mat'],'file')
        
            load(['data/',num2str(n),'-',num2str(Raduis),'.mat'],'fc_p','vel') 
       
            count=count+1;
            data_fc(count)=fc_p;
            data_n(count)=n;
            data_dia(count)=2*Raduis;
            data_vel_rel(count)=sta_vel_rel(vel);
            
         end
     end
     
    data_vel_rel=data_vel_rel(1:count);                       %Relative velocity
    data_n=data_n(1:count);                                   %Number density
    data_dia=data_dia(1:count);                               %Diameter

    data_fc=data_fc(1:count);                                 %Collision rate
   
  
    data1=data_n.^2;
    data2=data_fc./data_vel_rel;
   
    p1=polyfit(data1,data2,1);
    coeff=[coeff;p1(1)];
end

%}

%{

loglog(data_n,data_fc,'r*')
hold on 
loglog(N,N.^2,'--')
grid on
xlim([1e-2,0.5e-1])

%}

