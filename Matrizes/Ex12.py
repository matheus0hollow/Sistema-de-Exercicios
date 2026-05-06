import numpy as np
matriz = np.random.randint(1,10, (3, 3))
print(matriz)
Transposta = matriz.T
print(Transposta)
igual = matriz == Transposta
V = False in igual
if V == True:
    print("As matrizes não sao iguais")
else:
    print("As matrizes sao iguais")