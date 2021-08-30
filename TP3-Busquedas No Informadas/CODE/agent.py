from numpy import fabs
from enviroment import*
from trees import*
class agent:
    def __init__(self,env):
        self.env=env
        self.sol=env
        self.posX=env.initposX
        self.posY=env.initposY
    
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
        x=self.posX
        y=self.posY
        QL=[]
        Nodo=TreeNode((self.posX,self.posY))
        QL.append(Nodo)
        self.env.piso[self.posX][self.posY]="N"
        solu=None
        while QL!=[]:
            ActNode=QL.pop(0)
            self.posX=ActNode.value[0]
            self.posY=ActNode.value[1]
            if self.env.piso[self.posX][self.posY]=="O":
                solu=ActNode
                break
            self.env.piso[self.posX][self.posY]="N"

            if self.arriba()!=False:
                if self.env.piso[self.posX][self.posY-1]=="O":
                    solu=ActNode
                    break
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
        return solu

        if solu!=None:
            self.sol.print_solution(solu)
        else:
            return

    def Busqueda_Profundidad(self,ProfLimit):
        x=self.posX
        y=self.posY
        Nodo=TreeNode((x,y))
        solu=self.Busqueda_ProfundidaR(ProfLimit,0,Nodo)
        if solu!=False:
            self.sol.print_solution(solu)
            return solu
        else:
            self.env.print_environment()
            return[]

    def Busqueda_ProfundidaR(self,ProfLimit,Prof,ActNode):
        if (Prof>=ProfLimit):
            return False
        if self.env.piso[ActNode.value[0]][ActNode.value[1]]=="O":
            return ActNode
        else:
            solu=False
            self.posX=ActNode.value[0]
            self.posY=ActNode.value[1]
            self.env.piso[ActNode.value[0]][ActNode.value[1]]="N"
            if self.arriba()!=False:
                NuevoNodo=TreeNode((self.posX,self.posY-1),ActNode)
                solu=self.Busqueda_ProfundidaR(ProfLimit,Prof+1,NuevoNodo)
                if solu!=False:
                    return solu
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
    def sorthelp(self,array):
        return array.value[2]
    def Busqueda_uniforme(self):
        x=self.posX
        y=self.posY
        QL=[]
        Nodo=TreeNode((self.posX,self.posY,1))
        QL.append(Nodo)
        self.env.piso[self.posX][self.posY]="N"
        solu=None
        while QL!=[]:
            ActNode=QL.pop(0)
            self.posX=ActNode.value[0]
            self.posY=ActNode.value[1]
            peso=ActNode.value[2]
            if self.env.piso[self.posX][self.posY]=="O":
                solu=ActNode
                break
            
            self.env.piso[self.posX][self.posY]="N"

            if self.arriba()!=False:
                if self.env.piso[self.posX][self.posY-1]=="O":
                    solu=ActNode
                    break
                Nodo=TreeNode((self.posX,self.posY-1,peso+1),ActNode)
                self.env.piso[self.posX][self.posY-1]="G"
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
        if solu!=None:
            self.sol.print_solution(solu)
        else:
            return





