from board import*
import time
from statistics import*
import matplotlib.pyplot as plt

solu=[]
estados=[]
times=[]
func=[]
queenss=8
for i in range(0,30):
    br=board(queenss,150)
    j=0
    start=time.time()
    for k in range(0,30):
        br.NewGeneration()
        sol=br.bestsol()
        print(sol.Fitness())
        func.append(sol.Fitness())
        if sol.Fitness()>=52:
            sol.printQ()
            solu.append(sol)
            estados.append(j)
            end=time.time()
            times.append(end-start)
            """plt.plot(func)
            plt.title("Variacion de la funcion GA 8 reinas")
            plt.show()"""
            break
        j+=1

plt.boxplot(times)
plt.title("Tiempo de resolucion AG")
plt.show()
print(estados)
print("Algoritmo Genetico")

print("Media de tiempo de resolución",mean(times))
print("Desviación estandar de tiempo de resolucion", stdev(times))
print("Porcentaje de soluciones",(len(solu)/30)*100)
print("Media de estados por resolución",mean(estados))
print("Desviacion estandar de estados por resolucion",stdev(estados))