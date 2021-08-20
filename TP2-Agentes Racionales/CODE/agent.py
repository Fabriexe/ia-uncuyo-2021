from enviroment import*

class agent:
    def __init__(self,env,life,x,y):
        self.env=env
        self.reslife=life
        self.posX=x
        self.posY=y
        self.cleaned=0

    def perspectiva(self):#Crea un array de acciones
        acciones=[]#Acciones posibles
        piso=self.env.is_dirty(self.posX,self.posY)#Si la casilla esta sucia la limpia, sino no hace nada
        if piso==True:
            self.suck()
        else:
            self.nada()
        X=self.env.sX
        Y=self.env.sY
        if self.posX>0 and self.posX<X-1:#Verifica que no se encuentre en las orillas y agrega a acciones derecha e izquierda
            acciones.append(1)
            acciones.append(2)
        elif self.posX==0:#Si se encuentra a la derecha del todo se agrega la accion izquierda
            acciones.append(2)
        else:
            acciones.append(1)#sino agrega la accion derecha
        if self.posY>0 and self.posY<Y-1:#Verifica que no se encuentre en las orillas y agrega las acciones arriba y abajo
            acciones.append(3)
            acciones.append(4)
        elif self.posY==0: #Si se encuentra abajo del todo agrega la accion subir
            acciones.append(3)
        else:#sino agrega la de bajar
            acciones.append(4)
        return acciones

    def nada(self):
        print("",end="")
    
    def suck(self):#Limpia y almacena las casillas limpiadas
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
        return("Lo limpiado es: "+str(self.cleaned)+" cuadriculas ")

    def think(self):#Piensa
        acci=self.perspectiva()#Sensa el entorno
        num=randint(0,len(acci)-1)#Se acciona un lugar al azar al cual dirigirse entre las acciones posibles
        if acci[num]==1:
            self.derecha()
        elif acci[num]==2:
            self.izquierda()
        elif acci[num]==3:
            self.arriba()
        elif acci[num]==4:
            self.abajo()
        else:
            self.nada()
        self.reslife-=1#Se le resta la vida
            

