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
inte=30
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
        """
        plt.plot(results)
        plt.title("Variacion de la funcion HC 8 reinas")
        plt.show()"""
plt.boxplot(timeHistory)
plt.title("Tiempo de resolución HC")

plt.show()

if len(Hcstat)>=2:
    print(Hc)
    print("Media tiempo de resolución",mean(timeHistory))
    print("Desviacion estandar de tiempo de resolución",stdev(timeHistory))
    print("Porcentaje de soluciones Optimas",(Hc/inte)*100)
    print("Media de estados por resolucion",mean(Hcstat))
    print("Desviación estandar de estados por resolución",stdev(Hcstat))
else:
    print("No se encontraron soluciones")

print("XXX")
print("Resultados Simulated")
SA=0
timeHistory=[]
SAstates=[]
for i in range(0,inte):
    br=board(queens)
    results=[]
    start=time.time()
    for j in range(0,100):
        val=br.annealing()
        results.append(val)
        if val==0:
            SAstates.append(i)
            break
    last=results.pop()
    end=time.time()
    if last==0:
        SA+=1
        timeHistory.append(end-start)
        results.append(last)
        """
        plt.plot(results)
        plt.title("variacion de la funcion SA 8 Reinas")
        plt.show()"""

if len(SAstates)>=2:
    print(SA)
    print("Media tiempo de resolución",mean(timeHistory))
    print("Desviacion estandar de tiempo de resolución",stdev(timeHistory))
    print("Porcentaje de soluciones Optimas",(SA/inte)*100)
    print("Media de estados por resolucion",mean(SAstates))
    print("Desviación estandar de estados por resolución",stdev(SAstates))
else:
    print("No se encontraron soluciones")

plt.boxplot(timeHistory)
plt.title("Tiempo de resolución SA")
plt.show()