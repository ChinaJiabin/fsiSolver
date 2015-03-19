                                  %number of picture
N=100;                               
imread_path=[];
imwrite_path=[];
image_name='rand10-8.29.gif';
delay_time=0.05;

wm={'overwrite','append'};
                                  %'overwrite' (the default) or 'append'. 
                                  % In append mode, imwrite adds a single frame to the existing file.   
     
for n=1:N
    
   a=imread([imread_path,sprintf('%05d.png',n)]);
   if ndims(a)==2                    %
       a=cat(3,a,a,a);
   end
   
   [b,c]=rgb2ind(a,256);             %
   
   if n==1;
        imwrite(b,c,[imwrite_path,image_name],'Loopcount',inf,'DelayTime',delay_time,'WriteMode',wm{1+(n>1)});
   else
        imwrite(b,c,[imwrite_path,image_name],'DelayTime',delay_time,'WriteMode',wm{1+(n>1)});
   end
   
end