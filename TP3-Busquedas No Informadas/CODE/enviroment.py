from random import randint
import numpy as np #Crea arreglos y matrices llenas de 1 o 0
class environment:
    piso=[[]] #asignamos que va a ser una matriz
    def __init__(self,sX,sY,obstR):
        self.sX=sX
        self.sY=sY
        self.obstR=obstR
        self.initposX=randint(0,sX-1)#Selecciona una posicion random del agente en X
        self.initposY=randint(0,sY-1)#Selecciona una posicion random del agente en Y
        self.objposX=randint(0,sX-1)#Seleccion una posicion random del objetivo en X
        self.objposY=randint(0,sY-1)#Seleccion una posicion random del objetivo en Y
        self.obs=int((sX*sY)*obstR)#Calcula la cantidad de casillas obstaculos
        if self.obstR==1:
            self.piso= np.full((sX,sY),"X")
        else:
            self.piso=np.full((sX,sY)," ")#Llena la matriz
            self.piso[self.initposX][self.initposY]="A"
            self.piso[self.objposX][self.objposY]="O"
            i=0
            while i<self.obs:
                dupla=[randint(0,sX-1),randint(0,sY-1)]#Llena la matriz con la "Obstaculos"
                if self.piso[dupla[0]][dupla[1]]==" ":
                    self.piso[dupla[0]][dupla[1]]="X"
                    i+=1
        return
    def its_obst(self,x,y):#Devuelve si la casilla se encuentra un obstaculo o no
        if self.piso[x][y]=="X":
            return True
        else:
            return False
        
    def print_environment(self):#Imprime el entorno
        largo=len(self.piso)
        for i in range(0,largo):
            print(self.piso[i])
            print(" ")
    
    def print_solution(self,UltNode):
        Nodo=UltNode
        Camino=[]
        while Nodo!=None:
            Camino.append(Nodo.value)
            Nodo=Nodo.parent
        for i in Camino:
            if self.piso[i[0]][i[1]]!="O":
                self.piso[i[0]][i[1]]="S"
        self.print_environment()
        print(Camino)

    def estados(self):
        cont=0
        for i in range(self.sX):
            for j in range(self.sY):
                if (self.piso[i][j]=="N"):
                    cont+=1
        return cont
