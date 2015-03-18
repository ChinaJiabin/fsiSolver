%画出时间序列A的频谱图
%A为数据矩阵:第一列为时间项；第二列为随时间变化的数据项

[L,~]=size(A);
T=A(2,1)-A(1,1);
Fs=1/T;
NFFT=2^nextpow2(L);
Y=fft(A(:,2),NFFT)/L;
%
f=Fs/2*linspace(0,1,NFFT/2+1);
y_mag=2*abs( Y(1:NFFT/2+1) );
y_ang=angle(  Y(1:NFFT/2+1) );
%
plot( f,y_mag );
figure;
plot( f,y_ang );


