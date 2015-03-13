
file_path_read = 'logFsi'
file_path_write= 'plot/time-num_iter.csv'

file_read = open(file_path_read, 'r')
file_write = open(file_path_write,'w')

lines = file_read.xreadlines()
file_write.write('time,num_iter\n') 

time='0,';
num_iter='0\n';
id_num_iter=0;

for l in lines:
   
    l=l.split(' ')
    #---------------------------------------------------------------------------------
    #1.iteration number in every time step
    if len(l)==5:
       if l[0]=='Time':  

          timeOld=time
          time=l[2]
          num_iterOld=num_iter
          num_iter=l[-1]

          if (timeOld != time) & (timeOld != '0,'): 
             file_write.write(timeOld+num_iterOld)         
    #---------------------------------------------------------------------------------
    #2.Residuals in every subiteration
    if len(l)==5:
       if (l[0]=='Current') & (l[2]=='residual'):
      
          if num_iter=='1\n':
             if num_iterOld != '0\n':
                file_write_residual.close()
             id_num_iter+=1
             file_write_residual = open('plot/residual'+str(id_num_iter)+'.csv','w')
             file_write_residual.write('num_iter,residual\n')

          file_write_residual.write(num_iter.replace('\n',',')+l[-1])
    #---------------------------------------------------------------------------------

file_read.close();
file_write.close();

         
