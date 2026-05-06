import numpy as np
matriz = np.random.randint(1,10, (4, 4))
print(matriz)
soma = 0
for i in matriz:
    soma += i[0]
print(soma)