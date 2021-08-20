from enviroment import*

class agent:
    def __init__(self,env,life,x,y):
        self.env=env
        self.reslife=life
        self.posX=x
        self.posY=y
        self.cleaned=0

    def perspectiva(self):
        acciones=[]
        piso=self.env.is_dirty(self.env,self.posX,self.posY)
        if piso==True:
            self.suck
        else:
            self.nada
        X=self.env.sX
        Y=self.env.sY
        if self.posX<0 and self.posX<X-1:
            acciones.append(1)
            acciones.append(2)
        elif self.posX==0:
            acciones.append(2)
        else:
            acciones.append(1)
        if self.posY<0 and self.posY<Y-1:
            acciones.append(3)
            acciones.append(4)
        elif self.posY==0:
            acciones.append(3)
        else:
            acciones.append(4)
        return acciones

    def nada(self):
        print("No realizo nada")
    
    def suck(self):
        self.env.clean(self.posX,self.posY)
        self.cleaned+=1
    
    def arriba(self):
        self.posY+=1

    def derecha(self):
        self.posX-=1

    def abajo(self):
        self.posY-=1

    def izquierda(self):
        self.posX+=1
    
    def performance(self):
        return("Lo limpiado es: "+str(self.cleaned)+" cuadriculas")

    def think(self):
        acci=self.perspectiva(self)
        num=randint(0,len(acci))
        if acci[num]==1:
            self.derecha
        elif acci[num]==2:
            self.izquierda
        elif acci[num]==3:
            self.arriba
        elif acci[num]==4:
            self.abajo
        else:
            self.nada
        self.reslife-=1
            

