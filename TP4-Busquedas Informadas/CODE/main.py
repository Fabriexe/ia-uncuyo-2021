from agent import*
from enviroment import*
import statistics

result=[]
for i in range(0,30):
    env=environment(100,100,0.3)
    agente=agent(env)
    resultado=agente.A()
    if resultado!=None:
        result.append(env.estados())

print(result)
print("La Media: ",statistics.mean(result))
print("La Desviacion: ", statistics.stdev(result))