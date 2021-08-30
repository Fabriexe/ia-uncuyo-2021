from numpy import fabs, sqrt
from enviroment import*
from trees import*
class agent:
    def __init__(self,env):
        self.env=env
        self.sol=env
        self.posX=env.initposX
        self.posY=env.initposY
    #Verifica si puede realizar un movimiento hacia abajo, arriba,derecha , izquierda verificando el estado de la celda si es N:Negro X:Obstaculo G:Gris
    def abajo(self):
        if self.posY+1<self.env.sY:
            if self.env.piso[self.posX][self.posY+1]=="N" or self.env.piso[self.posX][self.posY+1]=="X" or self.env.piso[self.posX][self.posY+1]=="G":
                return False
        else:
            return False
    def derecha(self):
        if self.posX+1<self.env.sX:
            if self.env.piso[self.posX+1][self.posY]=="N" or self.env.piso[self.posX+1][self.posY]=="X" or self.env.piso[self.posX+1][self.posY]=="G":
                return False
        else:
            return False
    def arriba(self):
        if self.posY>0:
            if self.env.piso[self.posX][self.posY-1]=="N" or self.env.piso[self.posX][self.posY-1]=="X" or self.env.piso[self.posX][self.posY-1]=="G":
                return False
        else:
            return False
    def izquierda(self):
        if self.posX>0:
            if self.env.piso[self.posX-1][self.posY]=="N" or self.env.piso[self.posX-1][self.posY]=="X" or self.env.piso[self.posX-1][self.posY]=="G":
                return False
        else:
            return False
    #Calcula la distancia aplicando H**2=C1**2+C2**2
    def distancia(self,x,y):
        ox=self.env.objposX
        oy=self.env.objposY
        Dx=abs(x-ox)
        Dy=abs(y-oy)
        #Hipotenusa
        Fn=sqrt(Dx**2+Dy**2)
        return Fn
    #Ayuda a la funcion Sort
    def sorthelp(self,array):
        return array.value[2]
    def A(self):
        #Creamos una arraylist
        QL=[]
        #Se encola el nodo con la distancia y la ubicacion
        Nodo=TreeNode((self.posX,self.posY,self.distancia(self.posX,self.posY)))
        QL.append(Nodo)
        solu=None
        while QL!=[]:
            #Desencola el primero que entro
            ActNode=QL.pop(0)
            #Actualiza la posicion
            self.posX=ActNode.value[0]
            self.posY=ActNode.value[1]
            #si no es la solucion sigue
            if self.env.piso[self.posX][self.posY]=="O":
                solu=ActNode
                break
            #Cambia el color de la celda a negra
            self.env.piso[self.posX][self.posY]="N"
            #si se puede realizar el movimiento, y no es el objetivo el nodo siguiente, encola el nodo siguiente con la distancia actualizada y con la funcion sort
            #los ordena del de menor distancia hasta el de mayor distancia
            if self.arriba()!=False:
                if self.env.piso[self.posX][self.posY-1]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX,self.posY-1,self.distancia(self.posX,self.posY-1)),ActNode)
                self.env.piso[self.posX][self.posY-1]="G"
                QL.append(Nodo)
                QL.sort(key=self.sorthelp)


            if self.derecha()!=False:
                if self.env.piso[self.posX+1][self.posY]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX+1,self.posY,self.distancia(self.posX+1,self.posY)),ActNode)
                self.env.piso[self.posX+1][self.posY]="G"
                QL.append(Nodo)
                QL.sort(key=self.sorthelp)

            if self.abajo()!=False:
                if self.env.piso[self.posX][self.posY+1]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX,self.posY+1,self.distancia(self.posX,self.posY-1)),ActNode)
                self.env.piso[self.posX][self.posY+1]="G"
                QL.append(Nodo)
                QL.sort(key=self.sorthelp)

            if self.izquierda()!=False:
                if self.env.piso[self.posX-1][self.posY]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX-1,self.posY,self.distancia(self.posX-1,self.posY)),ActNode)
                self.env.piso[self.posX-1][self.posY]="G"
                QL.append(Nodo)
                QL.sort(key=self.sorthelp)
        #Printea la solucion
        if solu!=None:
            self.sol.print_solution(solu)
        else:
            return
        return solu




