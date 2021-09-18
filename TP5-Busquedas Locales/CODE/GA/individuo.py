from queen import*
from random import randint
import numpy as np

class individuo:
    
    def __init__(self,queens):
        self.cant=queens
        self.queens=[]
        for i in range(0,self.cant):
            NQ=Queen(i,randint(0,self.cant-1),self)
            self.queens.append(NQ)

    def Fitness(self):
        attack=0
        for i in self.queens:
            i.calcqueenpos(self.queens)
            attack+=i.Attac
        self.fitness=attack
        self.getfit=(self.cant**2)-self.fitness
        return((self.cant**2)-self.fitness)

    def printQ(self):
        board=np.full((self.cant,self.cant)," ")
        for i in range (self.cant):
            Q=self.queens[i]
            board[Q.posX][Q.posY]="Q"
        for i in range(self.cant):
            print("[|",end="")
            for j in range(self.cant):
                print(board[j][i],end=" |")
            print("]")
