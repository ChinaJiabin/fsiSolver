Dia=1e-3;
area=40*40*1e-6;
N=9;

data_1=zeros(N,1);
data_2=zeros(N,1);
data_mm=zeros(N,1);

count=0;
coef=[];

for i=480:40:800%[320,360,400,440,520,600,640,720]
    
    load([num2str(i),'.mat'])
    mm_vel_serial=mm_vel_serial/1000;
    max_nd=max(nd_serial);

    id=nd_serial>=(0.9*max_nd);
    id_=find(id);
    id_max=id_(end);
    id_min=id_(1);

    delta_t=time_serial(id_max)-time_serial(id_min);
    Nc=id_max-id_min+1;
    Nc=Nc/(delta_t*area);

    rel_vel=mean( rel_vel_serial(id_min:id_max) );
    mm_vel=mean( mm_vel_serial(id_min:id_max) );
    
    nd=mean( nd_serial(id_min:id_max) );
    nd=nd/area;
    
    count=count+1;
    data_1(count)=nd^2;
    data_2(count)=Nc/(rel_vel*Dia);
    data_mm(count)=Nc/(mm_vel*Dia);
    
    %p1=polyfit(mm_vel_serial(id_min:id_max),rel_vel_serial(id_min:id_max),1);
    p1=corrcoef(mm_vel_serial(id_min:id_max),rel_vel_serial(id_min:id_max));
    coef=[coef;p1(2,1)];
end

while ~isempty(id)
    
    id=find( diff(data_1)<0 )+1;
    data_1(id)=[];
    data_2(id)=[];
    
end

