from board import*
import time
from statistics import*
import matplotlib.pyplot as plt
print("Hill Climbing ")
print("")

Hc=0
timeHistory=[]
Hcstat=[]
queens=8
inte=60
results=[]

for i in range(0,inte):
    br=board(queens)
    results=[]
    start=time.time()
    for j in range(0,100):
        val=br.HC()
        results.append(val)
        if val==0:
            Hcstat.append(j)
            break
    last=results.pop()
    end=time.time()
    if last==0:
        Hc+=1
        timeHistory.append(end-start)
        results.append(last)
        plt.plot(results)
        plt.title("Variacion de la funcion Hc")
        plt.show

if len(Hcstat)>=2:
    print(Hc)
    print("Media tiempo de resolución",mean(timeHistory))
    print("Desviacion estandar de tiempo de resolución",stdev(timeHistory))
    print("Porcentaje de soluciones Optimas",(Hc/inte)*100)
    print("Media de estados por resolucion",mean(Hcstat))
    print("Desviación estandar de estados por resolución",stdev(Hcstat))
else:
    print("No se encontraron soluciones")