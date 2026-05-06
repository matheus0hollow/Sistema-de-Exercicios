import numpy as np
matriz = np.random.randint(1,10, (4, 4))
numero = int(input("Digite um numero: "))
print(matriz)
X = numero in matriz
if X == True:
    print("Esse numero esta na matriz")
else:
    print("Esse numero nao esta na matriz")