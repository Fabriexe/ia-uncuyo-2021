from math import trunc
from random import randint
import numpy as np
class environment:
    piso=[[]]
    def __init__(self,sX,sY,dirtR):
        self.sX=sX
        self.sY=sY
        self.dirtR=dirtR
        self.initposX=randint(0,sX-1)
        self.initposY=randint(0,sY-1)
        self.dirt=int((sX*sY)*dirtR)
        if self.dirtR==1:
            self.piso= np.ones((sX,sY))
        else:
            self.piso=np.zeros((sX,sY))
        self.piso[self.initposX][self.initposY]=2
        i=0
        while i<self.dirt:
            dupla=[randint(0,sX-1),randint(0,sY-1)]
            if self.piso[dupla[0]][dupla[1]]==0:
                self.piso[dupla[0]][dupla[1]]==1
                i+=1
        return
    def is_dirty(self,x,y):
        if self.piso[x][y]==1:
            return True
        else:
            return False
    def clean(self,x,y):
        self.piso[x,y]=0
        
    def print_environment(self):
        largo=len(self.piso)
        for i in range(largo):
            print(self.piso[i])
            print("")



