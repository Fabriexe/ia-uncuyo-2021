from queen import*
from individuo import*
from random import*
import numpy as np

class board:
    def __init__(self,queens,populatio):
        self.queens=[]
        self.cant=queens
        self.Plen=populatio
        self.population=[]
        self.prevg=round(populatio/4)
        for i in range(0,self.Plen):
            NI=individuo(self.cant)
            self.population.append(NI)
    
    def NewGeneration(self):
        NG=[]
        child=[]
        p1=0
        p2=0
        for i in range(0,self.Plen):
            while p1==p2:
                p1=self.Rselect()
                p2=self.Rselect()
            Nchild=self.Cross(p1,p2)
            self.mutation(Nchild[0])
            self.mutation(Nchild[1])
            child.extend(Nchild)
        child.extend(self.population)
        child.sort(reverse=True,key=lambda i : i.Fitness())
        for i in range(0,self.Plen):
            NG.append(child[i])
        self.population=NG
    
    def Rselect(self,p1=None):
        Maxfit=0
        for i in self.population:
            Maxfit+= i.Fitness()
        i=0
        j=True
        while j!=False: 
            if i==self.Plen-1:
                i=0
            Slec=self.population[i]
            prob=random()
            fitpro=(Slec.Fitness())/Maxfit
            if prob<fitpro:
                return Slec
            i+=1
    
    def Cross(self,I1,I2):
        I1Q=I1.queens
        I2Q=I2.queens

        child1=individuo(self.cant)
        child2=individuo(self.cant)
        child1.queens=[]
        child2.queens=[]
        div=round(self.cant/2)
        for i in range(0,self.cant):
            if i<div:
                child1.queens.append(I1Q[i])
                child2.queens.append(I2Q[i])
            else:
                child1.queens.append(I2Q[i])
                child2.queens.append(I1Q[i])
        return(child1,child2)
    
    def mutation(self,indiv):
        prob=0.1
        Q=indiv.queens[randint(0,self.cant-1)]
        rando=random()
        if rando<=prob:
            Q.posY=randint(0,self.cant-1)
        return indiv
    
    def printPopu(self):
        for i in self.population:
            i.printQ()
            print("")

    def bestsol(self):
        max=0
        Bi=None
        for i in self.population:
            if i.Fitness()>max:
                max=i.Fitness()
                Bi=i
        return Bi

    def calcular(self):
        larg=self.cant
        for i in range(larg):
            self.queens[i].calcColum(self.queens)
            
    def atacadas(self):
        At=0
        for i in range(self.cant):
            At+=self.queens[i].Attac-1
        return At/2


