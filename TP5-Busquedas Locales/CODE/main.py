from board import*

Board=board(8)
Board.printboard()

for i in range(0,5000):
    j=Board.annealing()
    if j==0:
        print("llegue a las",i)
        break
print("Fin")
Board.printboard()