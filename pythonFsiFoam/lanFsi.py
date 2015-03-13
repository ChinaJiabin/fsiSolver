import os
from numpy import *

class fsiAlgorithm:
   
   __filesPath   = "fsi/"
   __prePoints   = array([])
   __points      = array([])
   __residual    = array([])
   __subTimeStep = 0
   
   def __init__(self):
       self.__prePoints   = self.__readFiles(self.__filesPath+"prePoints")
       self.__points      = self.__readFiles(self.__filesPath+"points") 
       self.__residual    = self.__readFiles(self.__filesPath+"res")
      
       if os.path.exists(self.__filesPath+'time'):
	  self.__subTimeStep =int(self.__readScalar(self.__filesPath+'time'))         
       self.__subTimeStep+=1
       self.__writeFiles(self.__filesPath+'time',[[self.__subTimeStep]])
    
   #-----------------------------------------------------------------------------------------------------------------------------------------------------------
   #For different iteration method used for fluid-solid interaction
   def FixedPoint(self):
      rel = self.__readScalar(self.__filesPath+"rel")
      num = self.__points.size
      newPoints = self.__points+rel*self.__residual
      self.__writeFiles(self.__filesPath+"rel",[[rel]])
      self.__writeFiles(self.__filesPath+"newPoints",newPoints.reshape([num,1]))
      
      return newPoints
       
   def Aitken(self,maxRel):
      
      if self.__subTimeStep == 1:
	newPoints=self.FixedPoint()
      else:	
	rel         = self.__readScalar(self.__filesPath+"rel")
	pointsOld   = self.__readFiles(self.__filesPath+"pointsOld")
	residualOld = self.__readFiles(self.__filesPath+"resOld")
	
	rel = -sum((self.__points-pointsOld)*(self.__residual-residualOld)) \
              /sum((self.__residual-residualOld)**2 )  
        rel = sign(rel)*min(abs(rel),maxRel) 

	num = self.__points.size
	newPoints = self.__points+rel*self.__residual
	self.__writeFiles(self.__filesPath+"rel",[[rel]])
	self.__writeFiles(self.__filesPath+"newPoints",newPoints.reshape([num,1]))
	
      self.__writeFiles(self.__filesPath+"pointsOld",self.__points)
      self.__writeFiles(self.__filesPath+"resOld",self.__residual)

      return newPoints
      
   def IQN_ILS(self,maxNumColumn):
      if self.__subTimeStep == 1:
	newPoints=self.FixedPoint()
      else:
	#----------------------------------------------------------------------------------
	prePointsOld   =self.__readFiles(self.__filesPath+"prePointsOld")
	residualOld    =self.__readFiles(self.__filesPath+"resOld")
	#----------------------------------------------------------------------------------
	vMatrix = self.__readFiles(self.__filesPath+"vMatrix",maxNumColumn) 
	wMatrix = self.__readFiles(self.__filesPath+"wMatrix",maxNumColumn) 
	num = self.__points.size
	if len(vMatrix):  
	  vMatrix = hstack([(residualOld.reshape([num,1]) - self.__residual.reshape([num,1]) ), vMatrix] )
	  wMatrix = hstack([(prePointsOld.reshape([num,1])- self.__prePoints.reshape([num,1])), wMatrix] )
	else:
	  vMatrix = (residualOld.reshape([num,1]) - self.__residual.reshape([num,1]) )
	  wMatrix = (prePointsOld.reshape([num,1])- self.__prePoints.reshape([num,1]))  
	#----------------------------------------------------------------------------------
	vVector     = -self.__residual.reshape([num,1])
	q,r         = linalg.qr(vMatrix) 
	deltaPoints = dot( wMatrix,linalg.solve( r , dot(q.T,vVector) ) ) - vVector  
	newPoints   = self.__points.reshape([num,1]) + deltaPoints
        #----------------------------------------------------------------------------------
        self.__writeFiles(self.__filesPath+"vMatrix",vMatrix)
        self.__writeFiles(self.__filesPath+"wMatrix",wMatrix)
      	#----------------------------------------------------------------------------------
      self.__writeFiles(self.__filesPath+"prePointsOld",self.__prePoints)
      self.__writeFiles(self.__filesPath+"resOld",self.__residual)
      self.__writeFiles(self.__filesPath+"newPoints",newPoints)
      
      return newPoints
      
   def GMRES(self,numIter): 
    
    pMatrix = self.__readFiles(self.__filesPath+"pMatrix") 
    num = self.__points.size
    if len(pMatrix):
      pMatrix = hstack([pMatrix,self.__points.reshape([num,1])] )
    else:
      pMatrix = hstack([self.__pointsOld.reshape([num,1]),self.__points.reshape([num,1])])
      
    if self.__subTimeStep%numIter:
      #--------------------------------------------------------- 
      newPoints=self.FixedPoint()
      self.__writeFiles(self.__filesPath+"pMatrix",pMatrix)
      #---------------------------------------------------------  
    else:
      #---------------------------------------------------------  
      #GMRES
      rMatrix = diff(pMatrix)
      AMatrix = dot( (rMatrix.T)[0:-1], ((rMatrix.T)[0:-1]).T )
      BMatrix = dot( (rMatrix.T)[0:-1], ((rMatrix.T)[-1])     )
      BMatrix.shape =(1,len(pMatrix[0])-2)
      BMatrix=BMatrix.T
      
      alpha=linalg.solve(AMatrix - dot( BMatrix,array([[1]*(len(pMatrix[0])-2)]) ),-BMatrix)
      alpha=vstack([alpha,1-sum(alpha)])
    
      newPoints = dot( ((pMatrix.T)[0:-1]).T,alpha )
      self.__writeFiles(self.__filesPath+"pMatrix",newPoints)
      self.__writeFiles(self.__filesPath+"newPoints",newPoints)
      #---------------------------------------------------------        
    return newPoints
   
   def mixAitken_IQN(self,maxRel,maxNumColumn,numSubStepsForAitken):
     
     if self.__subTimeStep < numSubStepsForAitken:
       newPoints=self.Aitken(maxRel)  
     else: 
       if self.__subTimeStep == numSubStepsForAitken:
         newPoints=self.Aitken(maxRel)
         self.__writeFiles(self.__filesPath+"prePointsOld",self.__prePoints)
       else:
         newPoints=self.IQN_ILS(maxNumColumn)
         
     return newPoints
     
   def IQNFixRelaxing(self,rel,maxNumColumn):
     
     if self.__subTimeStep == 1:
	newPoints=self.FixedPoint()
     else:
	#----------------------------------------------------------------------------------
	prePointsOld   =self.__readFiles(self.__filesPath+"prePointsOld")
	residualOld    =self.__readFiles(self.__filesPath+"resOld")
	#----------------------------------------------------------------------------------
	vMatrix = self.__readFiles(self.__filesPath+"vMatrix",maxNumColumn) 
	wMatrix = self.__readFiles(self.__filesPath+"wMatrix",maxNumColumn) 
	num = self.__points.size
	if len(vMatrix):  
	  vMatrix = hstack([(residualOld.reshape([num,1]) - self.__residual.reshape([num,1]) ), vMatrix] )
	  wMatrix = hstack([(prePointsOld.reshape([num,1])- self.__prePoints.reshape([num,1])), wMatrix] )
	else:
	  vMatrix = (residualOld.reshape([num,1]) - self.__residual.reshape([num,1]) )
	  wMatrix = (prePointsOld.reshape([num,1])- self.__prePoints.reshape([num,1]))  
	#----------------------------------------------------------------------------------
	vVector     = -self.__residual.reshape([num,1])
	q,r         = linalg.qr(vMatrix) 
	deltaPoints = dot( wMatrix,linalg.solve( r , dot(q.T,vVector) ) ) - vVector  
	
	Rel = min(1,rel*self.__subTimeStep)
	newPoints   = self.__points.reshape([num,1]) + Rel*deltaPoints
        #----------------------------------------------------------------------------------
        self.__writeFiles(self.__filesPath+"vMatrix",vMatrix)
        self.__writeFiles(self.__filesPath+"wMatrix",wMatrix)
      	#----------------------------------------------------------------------------------
     self.__writeFiles(self.__filesPath+"prePointsOld",self.__prePoints)
     self.__writeFiles(self.__filesPath+"resOld",self.__residual)
     self.__writeFiles(self.__filesPath+"newPoints",newPoints)
     
   def IQNVarRelaxing(self,maxRel,maxNumColumn): 
   
     if self.__subTimeStep == 1:
        rel = self.__readScalar(self.__filesPath+"rel")
        num = self.__points.size
        newPoints = self.__points+rel*self.__residual
        self.__writeFiles(self.__filesPath+"rel",[[rel]])
        self.__writeFiles(self.__filesPath+"newPoints",newPoints.reshape([num,1]))
        self.__writeFiles(self.__filesPath+"deltaPointsOld",self.__residual)
     else:
	#----------------------------------------------------------------------------------
	pointsOld       = self.__readFiles(self.__filesPath+"pointsOld")
	prePointsOld    = self.__readFiles(self.__filesPath+"prePointsOld")
	deltaPointsOld =  self.__readFiles(self.__filesPath+"deltaPointsOld")
	residualOld     = self.__readFiles(self.__filesPath+"resOld")
	#----------------------------------------------------------------------------------
	vMatrix = self.__readFiles(self.__filesPath+"vMatrix",maxNumColumn) 
	wMatrix = self.__readFiles(self.__filesPath+"wMatrix",maxNumColumn) 
	num = self.__points.size
	if len(vMatrix):  
	  vMatrix = hstack([(residualOld.reshape([num,1]) - self.__residual.reshape([num,1]) ), vMatrix] )
	  wMatrix = hstack([(prePointsOld.reshape([num,1])- self.__prePoints.reshape([num,1])), wMatrix] )
	else:
	  vMatrix = (residualOld.reshape([num,1]) - self.__residual.reshape([num,1]) )
	  wMatrix = (prePointsOld.reshape([num,1])- self.__prePoints.reshape([num,1]))  
	#----------------------------------------------------------------------------------
	vVector     = -self.__residual.reshape([num,1])
	q,r         = linalg.qr(vMatrix) 
	deltaPoints = dot( wMatrix,linalg.solve( r , dot(q.T,vVector) ) ) - vVector
	
	#----------------------------------------------------------------------------------
	#Calculate rel
	rel = -sum( (self.__points-pointsOld).reshape([num,1])*( deltaPoints-deltaPointsOld.reshape([num,1]) ) ) \
              /sum((deltaPoints-deltaPointsOld.reshape([num,1]))**2 )
        rel = sign(rel)*min(abs(rel),maxRel) 
        print rel
        #----------------------------------------------------------------------------------
	newPoints   = self.__points.reshape([num,1]) + rel*deltaPoints
        #----------------------------------------------------------------------------------
        
        self.__writeFiles(self.__filesPath+"vMatrix",vMatrix)
        self.__writeFiles(self.__filesPath+"wMatrix",wMatrix)
        self.__writeFiles(self.__filesPath+"deltaPointsOld",deltaPoints)
      	#----------------------------------------------------------------------------------
     self.__writeFiles(self.__filesPath+"pointsOld",self.__points)
     self.__writeFiles(self.__filesPath+"prePointsOld",self.__prePoints)
     self.__writeFiles(self.__filesPath+"resOld",self.__residual)
     self.__writeFiles(self.__filesPath+"newPoints",newPoints)
      
   #-----------------------------------------------------------------------------------------------------------------------------------------------------------
   #For IO   
   def __readScalar(self,filesPath):
    if os.path.exists(filesPath) == False:
       return []
    f = open(filesPath,'r')
    var = float(f.readline()) 
    f.close()
    return var
    
   def __readFiles(self,filesPath,num_column = 0 ):
    var = []
    if os.path.exists(filesPath) == False:
       return array(var)
    f   = open(filesPath,'r')
    for line in f:
        line = line.split('\t')
        line.pop()
        #
        temp = []
        for i in range(len(line)):
	   if num_column:
	      if i == num_column-1:
		  break
           temp.append(float(line[i]))
        var.append(temp)
        #
    f.close()
    return array(var)
       
   def __writeFiles(self,filesPath,data):
    f= open(filesPath,'w')
    for line in data:
        for l in line:
            f.write(str(l)+'\t')
        f.write('\n')
    f.close()
    
   #-----------------------------------------------------------------------------------------------------------------------------------------------------------
   #end
