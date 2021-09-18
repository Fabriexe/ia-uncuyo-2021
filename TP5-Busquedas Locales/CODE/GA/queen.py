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

