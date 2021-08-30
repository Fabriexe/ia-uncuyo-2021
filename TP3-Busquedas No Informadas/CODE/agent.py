from numpy import fabs
from enviroment import*
from trees import*
class agent:
    def __init__(self,env):
        self.env=env
        self.sol=env
        self.posX=env.initposX
        self.posY=env.initposY
    #Verifica si puede moverse en las direcciones verificando las celdas que estas no sean N:Negra, X:Obstaculo G:Gris
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

    def Busqueda_Anchura(self):
        #Creamos una arraylist y encolamos la posicion
        QL=[]
        Nodo=TreeNode((self.posX,self.posY))
        QL.append(Nodo)
        solu=None
        while QL!=[]:
            #Se saca el primer nodo que entra
            ActNode=QL.pop(0)
            self.posX=ActNode.value[0]
            self.posY=ActNode.value[1]
            #Guardamos la posicion nueva, si la posicion no es el objetivo, sigue
            if self.env.piso[self.posX][self.posY]=="O":
                solu=ActNode
                break
            #Cambiamos el color a gris
            self.env.piso[self.posX][self.posY]="N"
            #Verifica si se pueden realizar el movimiento, si es asi verifica si no es el objetivo
            if self.arriba()!=False:
                if self.env.piso[self.posX][self.posY-1]=="O":
                    solu=ActNode
                    break
                #Crea un nuevo nodo hijo del actual y lo pinta de Gris y lo encola
                Nodo=TreeNode((self.posX,self.posY-1),ActNode)
                self.env.piso[self.posX][self.posY-1]="G"
                QL.append(Nodo)

            if self.derecha()!=False:
                if self.env.piso[self.posX+1][self.posY]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX+1,self.posY),ActNode)
                self.env.piso[self.posX+1][self.posY]="G"
                QL.append(Nodo)

            if self.abajo()!=False:
                if self.env.piso[self.posX][self.posY+1]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX,self.posY+1),ActNode)
                self.env.piso[self.posX][self.posY+1]="G"
                QL.append(Nodo)

            if self.izquierda()!=False:
                if self.env.piso[self.posX-1][self.posY]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX-1,self.posY),ActNode)
                self.env.piso[self.posX-1][self.posY]="G"
                QL.append(Nodo)
        
        #Si encuentra la solucion la printea y la devuelve 
        if solu!=None:
            self.sol.print_solution(solu)
        else:
            return []
        return solu

    def Busqueda_Profundidad(self,ProfLimit):
        #Con profundidad limite
        x=self.posX
        y=self.posY
        Nodo=TreeNode((x,y))
        #Manda a la funcion recursiva el nodo que guarda con un peso de 0
        solu=self.Busqueda_ProfundidaR(ProfLimit,0,Nodo)
        #si encuentra la solucion printea, sino retorna la lista vacia
        if solu!=False:
            self.sol.print_solution(solu)
            return solu
        else:
            self.env.print_environment()
            return[]

    def Busqueda_ProfundidaR(self,ProfLimit,Prof,ActNode):
        #Si la profundidad es mayor al limite retorna false
        if (Prof>=ProfLimit):
            return False
        #si el nodo es el objetivo retorna el nodo
        if self.env.piso[ActNode.value[0]][ActNode.value[1]]=="O":
            return ActNode
        else:
            solu=False
            #Guarda la posicion, y la colorea Negra
            self.posX=ActNode.value[0]
            self.posY=ActNode.value[1]
            self.env.piso[ActNode.value[0]][ActNode.value[1]]="N"
            #Verifica si se puede mover arriba
            if self.arriba()!=False:
                #Crea un nuevo nodo con la posicion hacia arriba y manda ese nodo a la recursividad
                NuevoNodo=TreeNode((self.posX,self.posY-1),ActNode)
                solu=self.Busqueda_ProfundidaR(ProfLimit,Prof+1,NuevoNodo)
                if solu!=False:
                    return solu
            #Vuelve a la posicion que estaba 
            self.posX=ActNode.value[0]
            self.posY=ActNode.value[1]
            if self.abajo()!=False:
                NuevoNodo=TreeNode((self.posX,self.posY+1),ActNode)
                solu=self.Busqueda_ProfundidaR(ProfLimit,Prof+1,NuevoNodo)
                if solu!=False:
                    return solu
            self.posX=ActNode.value[0]
            self.posY=ActNode.value[1]
            if self.izquierda()!=False:
                NuevoNodo=TreeNode((self.posX-1,self.posY),ActNode)
                solu=self.Busqueda_ProfundidaR(ProfLimit,Prof+1,NuevoNodo)
                if solu!=False:
                    return solu
            self.posX=ActNode.value[0]
            self.posY=ActNode.value[1]
            if self.derecha()!=False:
                NuevoNodo=TreeNode((self.posX+1,self.posY),ActNode)
                solu=self.Busqueda_ProfundidaR(ProfLimit,Prof+1,NuevoNodo)
                if solu!=False:
                    return solu
            return solu
    #ayuda a la funcion sort
    def sorthelp(self,array):
        return array.value[2]
    def Busqueda_uniforme(self):
        QL=[]
        #Se crea un nodo con un peso de 1
        Nodo=TreeNode((self.posX,self.posY,1))
        QL.append(Nodo)
        solu=None
        while QL!=[]:
            #Desencola el nodo
            ActNode=QL.pop(0)
            self.posX=ActNode.value[0]
            self.posY=ActNode.value[1]
            #Guardamos el peso
            peso=ActNode.value[2]
            #si es la solucion retorna
            if self.env.piso[self.posX][self.posY]=="O":
                solu=ActNode
                break
            #Colorea a Negro el nodo
            self.env.piso[self.posX][self.posY]="N"
            #Si es posible realizar el movimiento lo realiza, si llega al objetivo retorna,
            if self.arriba()!=False:
                if self.env.piso[self.posX][self.posY-1]=="O":
                    solu=ActNode
                    break
                #Crea un nodo hijo con el peso+1 y lo colorea de Gris
                Nodo=TreeNode((self.posX,self.posY-1,peso+1),ActNode)
                self.env.piso[self.posX][self.posY-1]="G"
                #Lo encola y ordena la lista por pesos
                QL.append(Nodo)
                QL.sort(key=self.sorthelp)


            if self.derecha()!=False:
                if self.env.piso[self.posX+1][self.posY]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX+1,self.posY,peso+1),ActNode)
                self.env.piso[self.posX+1][self.posY]="G"
                QL.append(Nodo)
                QL.sort(key=self.sorthelp)

            if self.abajo()!=False:
                if self.env.piso[self.posX][self.posY+1]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX,self.posY+1,peso+1),ActNode)
                self.env.piso[self.posX][self.posY+1]="G"
                QL.append(Nodo)
                QL.sort(key=self.sorthelp)

            if self.izquierda()!=False:
                if self.env.piso[self.posX-1][self.posY]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX-1,self.posY,peso+1),ActNode)
                self.env.piso[self.posX-1][self.posY]="G"
                QL.append(Nodo)
                QL.sort(key=self.sorthelp)
        #Si encuentra la solucion la printea
        if solu!=None:
            self.sol.print_solution(solu)
        else:
            return[]
        return solu




