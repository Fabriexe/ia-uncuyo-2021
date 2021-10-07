import numpy as np
from trees import*
import copy
estados=0
def fcdfs(Node,Board,queencant):
    if Node.height+1==queencant:
        result=camino(Node)
        printboard(queencant,result)
        return(result)
    else:
        altura=Board[Node.height+1]
        for e in range (len(altura)):
            Nboard=copy.deepcopy(Board)
            Nodo=TreeNode(e,Node.height+1,Node)
            estados=fowacheck(Nodo,Nboard)
            if Nboard==False:
                return None
            result=fcdfs(Nodo,Nboard,queencant)
            if result!=None:
                return(result,estados)

def fowacheck(Nodo,Board):
    global estados
    colum=Nodo.value
    altu=Nodo.height
    estados+=1
    for i in range(len(Board)):
        Fil=Board[i]
        largo=len(Fil)
        j=0
        while j<largo:
            Val=Fil[j]
            if i!=altu:
                if Val==colum:
                    Fil.remove(colum)
                    j-=1
                    largo-=1
                elif abs(Val-colum)==abs(i-altu):
                    Fil.remove(Val)
                    j-=1
                    largo-=1
            j+=1
        if len(Fil)==0:
            return False
    return True


def camino(UltNode):
        Nodo=UltNode
        Camino=[]
        while Nodo!=None:
            Camino.append(Nodo)
            Nodo=Nodo.parent
        return Camino

def printboard(cant,camino):
    board=np.full((cant,cant)," ")
    for i in range (len(camino)):
        Q=camino[i]
        board[Q.value][Q.height]="Q"
    for i in range(cant):
        print("[|",end="")
        for j in range(cant):
            print(board[j][i],end=" |")
        print("]")