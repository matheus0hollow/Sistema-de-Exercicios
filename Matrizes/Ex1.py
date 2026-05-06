import numpy as np
x = np.random.randint(1,10, (3, 3))
print(x)
soma = 0
numero = 0
for i in x:
    numero = np.sum(i)
    soma += numero
print(soma)