from numpy.lib.function_base import append
from enviroment import*
from agent import*
import statistics
resultA=[]
resultP=[]
resultU=[]

for i in range(0,30):
    env=environment(100,100,0.3)
    agente=agent(env)
    resultados=agente.Busqueda_Anchura()
    if resultados!=[]:
        resultA.append(env.estados())

print(resultA)
print("Media: ",statistics.mean(resultA))
print("Desviacion :",statistics.stdev(resultA))
print("")

for i in range(0,30):
    env=environment(100,100,0.3)
    agente=agent(env)
    resultados=agente.Busqueda_Profundidad(500)
    if resultados!=[]:
        resultP.append(env.estados())

print(resultP)
print("Media: ",statistics.mean(resultP))
print("Desviacion :",statistics.stdev(resultP))
print("")

for i in range(0,30):
    env=environment(100,100,0.3)
    agente=agent(env)
    resultados=agente.Busqueda_uniforme()
    if resultados!=[]:
        resultU.append(env.estados())
print(resultU)
print("Media: ",statistics.mean(resultU))
print("Desviacion :",statistics.stdev(resultU))
print("")


