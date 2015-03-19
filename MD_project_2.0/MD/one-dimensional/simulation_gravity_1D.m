%Molecular Dynamics Simulation of Hard Spheres in one dismension
%Considering the influence of gravity

%--------------------------------------------------------------------------
%0.Parameter
   geometry;
   generator;
   parameter;
  
%--------------------------------------------------------------------------
%1.Establish a priority queue of future event
   fprintf('Establish a priority queue of future event\n\n\n')
   
     %Collision between particle and a wall       
     for k=1
         Colwall_gravity;
     end
     
     %Collision between two particles     
     for i=1:N-1
         for j=i+1
             Colparticles;
         end
     end

fprintf('Start simulation\n\n\n')

while time<time_end && count>0 && N>0
      show_simulation_information;
%--------------------------------------------------------------------------  
%2.Move particles and file output 
      Move_gravity;

                        %----Optional Jobs-----
                        %     Statistics;
                        %----------------------
                        
%--------------------------------------------------------------------------
%3.Adjust queue of future events  
     Adjust_queue;
    
%--------------------------------------------------------------------------    
%4.Event happens and find new future events
     if mark_j<0  
        %Event happens
        Collision_wall;
        
        %Collision between particle and a wall
        k=1;
        Colwall_gravity; 
        
        
        %Collision between two particles
        i=1;
        j=2;           
        Colparticles;
                    
     else
         
        loop_count=loop_count+1;
        %Event happens 
        Collision_particles;
    
        %Collision between particle and a wall
        if min([mark_i,mark_j])==1
            k=1;
            Colwall_gravity; 
        end
       
        %Collision between two particles
        for i=[mark_i,mark_j]
            id=[i-1 i+1];
            id=id(id>=1);
            id=id(id<=N);
            for j=id
                Colparticles;
            end
        end
           
     end
end

%--------------------------------------------------------------------------  
%5.End
   show_final_information;
                        %----Optional Jobs-----
                        %    Statistics_End;
                        %----------------------
                        
%--------------------------------------------------------------------------  
