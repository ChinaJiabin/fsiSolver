function mgif(N)
%N=number of picture
wm={'overwrite','append'};
                                  %'overwrite' (the default) or 'append'. 
                                  % In append mode, imwrite adds a single frame to the existing file.                       
for n=0:N-1
a=imread(['C:\Users\jiabin\Documents\MATLAB\myMfile\monte carlo method\brownian\picture\'...
          ,sprintf('%04d.png',n)]);
if ndims(a)==2                    %ÔªËØÎ¬¶È
    a=cat(3,a,a,a);
end
[b,c]=rgb2ind(a,256);             %RGBÍ¼Ïñ×ª»¯ÎªË÷ÒıÍ¼Ïñ

imwrite(b,c,'C:\Users\jiabin\Documents\MATLAB\diffusion2.gif','DelayTime',0.08,'WriteMode',wm{1+(n>1)});
end
