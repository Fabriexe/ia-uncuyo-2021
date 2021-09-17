from queen import*
from random import randint
from math import*
import numpy as np

class board:
    def __init__(self,queens):
        self.queens=[]
        self.cant=queens
        self.t=1
        for i in range(0,self.cant):
            NQ=Queen(i,randint(0,self.cant-1),self)
            self.queens.append(NQ)
        for i in range(0,self.cant):
            self.queens[i].calcColum(self.queens)
        self.val=2*queens

    def calcular(self):
        larg=self.cant
        for i in range(larg):
            self.queens[i].calcColum(self.queens)
            
    def atacadas(self):
        At=0
        for i in range(self.cant):
            At+=self.queens[i].Attac-1
        return At/2

    def HC(self):
        MejorQ=None
        Bp=99999
        for i in range(self.cant-1):
            Qact=self.queens[i]
            Qpos=(Qact.Bpos)
            if Qpos[2]<=Bp:
                if Qact.posY!=Qpos[1] or Qact.posX!=Qpos[0]:
                    MejorQ=self.queens[i]
                    Bp=Qpos[2]
        if MejorQ!=None and Bp<=self.val:
            MejorQ.posX=MejorQ.Bpos[0]
            MejorQ.posY=MejorQ.Bpos[1]
            self.val=Bp
        self.calcular()
        return self.atacadas()

    def annealing(self):
        rand=randint(0,self.cant-1)
        self.t+=2
        Qact=self.queens[rand]
        pos=Qact.positions[randint(0,self.cant-2)]
        if pos[2]<= self.val:
            self.val=pos[2]
            Qact.posX=pos[0]
            Qact.posY=pos[1]
            self.calcular()
            return self.atacadas()
        else:
            probabilidad=randint(0,100)/100
            div= exp(abs(pos[2]-self.val)/self.t)/100
            if div>probabilidad:
                self.val=pos[2]
                Qact.posX=pos[0]
                Qact.posY=pos[1]
                self.calcular()
                return self.atacadas()
            else:
                return self.atacadas()

    def printboard(self):
        board=np.full((self.cant,self.cant)," ")
        for i in range (self.cant):
            Q=self.queens[i]
            pos=Q.positions
            board[Q.posX][Q.posY]="Q"
        for i in range(self.cant):
            print("[|",end="")
            for j in range(self.cant):
                print(board[j][i],end=" |")
            print("]")
