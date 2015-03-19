N_test=1;

for i=1:N_test
    
    for N_init=50:50:1000
        [n,fc,vel]=Simulation_Gravity_1D(N_init);
        save([num2str(i),'-',num2str(n)],'n','fc','vel')
    end
    
end