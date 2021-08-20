from random import randint
import numpy as np #Crea arreglos y matrices llenas de 1 o 0
class environment:
    piso=[[]] #asignamos que va a ser una matriz
    def __init__(self,sX,sY,dirtR):
        self.sX=sX
        self.sY=sY
        self.dirtR=dirtR
        self.initposX=randint(0,sX-1)#Selecciona una posicion random del agente en X
        self.initposY=randint(0,sY-1)#Selecciona una posicion random del agente en Y
        self.dirt=int((sX*sY)*dirtR)#Calcula la cantidad de casillas sucias
        if self.dirtR==1:
            self.piso= np.ones((sX,sY))
        else:
            self.piso=np.zeros((sX,sY))#Llena la matriz
            i=0
            while i<self.dirt:
                dupla=[randint(0,sX-1),randint(0,sY-1)]#Llena la matriz con la "suciedad"
                if self.piso[dupla[0]][dupla[1]]==0:
                    self.piso[dupla[0]][dupla[1]]=1
                    i+=1
        return
    def is_dirty(self,x,y):#Devuelve si la casilla se encuentra sucia o no
        if self.piso[x][y]==1:
            return True
        else:
            return False
    def clean(self,x,y):#Limpia la casilla
        self.piso[x,y]=0
        
    def print_environment(self):#Imprime el entorno
        largo=len(self.piso)
        for i in range(0,largo):
            print(self.piso[i])
            print("")
            
    def get_performance(self):#Obtiene la performance
        cont=0
        for i in range(self.sX-1):
            for j in range(self.sY-1):
                if self.piso[i][j]==1:#obtiene las casillas sucias
                    cont+=1
        return("La suciedad del entorno es del " +str((cont*100)/(self.sX*self.sY))+"%")#Regla de 3 simple y calcula el porcentaje


