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
        for i in self.queens:
            At+=i.Attac-1
        return At/2

    def HC(self):
        MejorQ=None
        Bp=99999
        for i in range(self.cant):
            Qact=self.queens[i]
            Qpos=(Qact.Bpos)
            if Qpos[2]<=Bp:
                if Qact.self.posY!=Qpos[1] or Qact.self.posX!=Qpos[0]:
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
        Qact=self.queens[rand]
        pos=self.positions[randint(0,self.cant-1)]
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
        board=np.zeros(self.cant,self.cant)
        for i in range (self.cant):
            Q=self.queens[i]
            board[Q.posX][Q.posY]="Q"
        for i in range(self.cant):
            for j in range(self.cant):
                if board[i][j]==0:
                    board[i][j]=" "
        for i in range(self.cant):
            print(board[i])
