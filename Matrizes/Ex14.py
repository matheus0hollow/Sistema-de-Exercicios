import numpy as np
matriz1 = np.random.randint(1,10, (2, 2))
matriz2 = np.random.randint(1,10, (2, 2))
print(matriz1)
print(matriz2)
mult = np.dot(matriz1, matriz2)
print(mult)