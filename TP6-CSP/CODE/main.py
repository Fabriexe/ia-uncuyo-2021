from backtrack import*
from forwardcheacking import*
import numpy as np
reinas=[4,8,10,12]
#b=[[i for i in range(reinas)]for j in range(reinas)]
#N=TreeNode(0,0)
#result=fcdfs(N,b,8)
times=[]
estados=[]
import time
import matplotlib.pyplot as plt
for i in reinas:
    start=time.time()
    result=dfs(i)
    end=time.time()
    times.append(end-start)
    estados.append(result[1])

print("Backtrack time", times)
print("Backtrack Estados",estados)
plt.boxplot(times)
plt.title("Tiempo de ejecucion backtracking")
plt.show()
plt.boxplot(estados)
plt.title("Estados backtracking")
plt.show()