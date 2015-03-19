%Molecular Dynamics Simulation of Hard Spheres
%Molecular moves in straight line

%--------------------------------------------------------------------------
%0.Parameter
   clear;
   geometry;
   genertor;
   parameter;
  
%--------------------------------------------------------------------------
%1.Establish a priority queue of future event
   fprintf('Establish a priority queue of future event\n\n\n')
     %Collision between particle and a wall       
     for k=1:N
         Colwall;
     end
     %Collision between two particles     
     for i=1:N
         for j=i+1:N
             Colparticles;
         end
     end

fprintf('Start simulation\n\n\n')
while time<time_end && count>0 && N>0
      show_simulation_information;
%--------------------------------------------------------------------------  
%2.Move particles and file output 
      Move;

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
        k=mark_i;
        Colwall;
           
        if -mark_j<N_empty_wall
           %Collision between two particles
           for i=1:N
               j=mark_i;
               Colparticles;
           end         
        end
       
     else
        %Event happens 
        Collision_particles;
    
        %Collision between particle and a wall
        for k=[mark_i,mark_j]
            Colwall; 
        end
        %Collision between two particles
        for i=1:N
            for j=[mark_i,mark_j]
                 Colparticles;
            end
        end
           
     end
end

%--------------------------------------------------------------------------  
%5.End
   show_final_information;
                        %----Optional Jobs-----
                        %   Statistics_End;
                        %----------------------
                        
%--------------------------------------------------------------------------  
