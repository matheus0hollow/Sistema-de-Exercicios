import numpy as np
matriz = np.random.randint(1,10, (3, 4))
print(matriz)
spar = 0
for i in matriz:
    for j in i:
        if j % 2 == 0:
            spar += 1
print(spar)