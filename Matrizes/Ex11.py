import numpy as np
matriz = np.random.randint(1,10, (3, 3))
print(matriz)
soma_colunas = np.sum(matriz, axis=0)
print(soma_colunas)