from agent import*
from enviroment import*
from randomagent import*

x=8
y=8
dirt=0.1

env1=environment(x,y,dirt)
env2=environment(x,y,dirt)

agente=agent(env1,1000,env1.initposX,env1.initposY)
agente2=randomagent(env2,1000,env2.initposX,env2.initposY)

print("Entorno Inicial Agente")
env1.print_environment

while agente.reslife>0:
    agente.think()

print("Entorno Final")
env1.print_environment

print("Entorno Inicial Agente Random")
env2.print_environment

while agente2.reslife>0:
    agente2.think()

print("Entorno Final")
env2.print_environment

print("Performance Agente: " + agente.performance()+" de:" +str(env1.dirt)+"cuadriculas sucias")
print(env1.get_performance())

print("Performance Agente Aleatorio: " + agente2.performance()+" de:" +str(env2.dirt)+"cuadriculas sucias")
print(env2.get_performance())