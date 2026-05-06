import numpy as np
matriz = np.random.randint(1,10, (5, 5))
print(matriz)
secundaria = []
for i in matriz:
    secundaria.append(i[1])
print(secundaria)