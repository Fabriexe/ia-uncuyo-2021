class Queen:
    def __init__(self,posX,posY,board):
        self.posX=posX
        self.posY=posY
        self.board=board
        self.positions=[]
        self.Bpos=(0,0,99999)
        self.Attac=0

    def calcqueenpos(self,queens):
        attack=0
        larg=len(queens)
        for i in range(larg):
            if self.posY==queens[i].posY:
                attack+=1
            elif abs(self.posX-queens[i].posX)==abs(self.posY-queens[i].posY):
                attack+=1
        self.Attac=attack

    def calcColum(self,queens):
        self.positions=[]
        larg=len(queens)
        for i in range(0,larg):
            if i!=self.posY:
                self.calcpos((self.posX,i),queens)
        self.calcqueenpos(queens)
    
    def calcpos(self,pos,queens):
        attack=0
        larg=len(queens)
        for i in range(0,larg):
            if pos[1]==queens[i].posY:
                attack+=2
            elif abs(pos[0]-queens[i].posX)==abs(pos[1]-queens[i].posY):
                attack+=2
        if attack<= self.Bpos[2]:
            self.Bpos=(pos[0],pos[1],attack)
        self.positions.append((pos[0],pos[1],attack))
