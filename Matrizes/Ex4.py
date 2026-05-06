import numpy as np
matriz = np.array([[4,5]
                 ,[6,7]])
matriz[[0, 1]] = matriz[[1, 0]]
print(matriz)