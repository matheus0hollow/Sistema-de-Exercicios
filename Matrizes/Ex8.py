import numpy as np
matriz = np.random.randint(1,10, (3, 3))
print(matriz)
med = []
for i in matriz:
    med.append(np.mean(i))
print(med)