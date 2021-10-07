from trees import*
import numpy as np
Queens=0
def dfs(queencant):
    estados=0
    root=TreeNode(2,0)
    cola=[root]
    while len(cola)>0:
        Nodo=cola.pop(0)
        estados+=1
        if (Nodo.height+1)==(queencant):
            result=camino(Nodo)
            printboard(queencant,result)
            return(result,estados)
        for i in range(0,queencant):
            if calcqueenpos(Nodo,i,Nodo.height+1)==True:
                Nuevo=TreeNode(i,Nodo.height+1,Nodo)
                cola.append(Nuevo)

def calcqueenpos(Nodo,fil,altu):
    Posi=camino(Nodo)
    for i in range(0,len(Posi)):
        CQ=Posi[i]
        if CQ.value==fil:
            return False
        if abs(CQ.value-fil)==abs(CQ.height-altu):
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


