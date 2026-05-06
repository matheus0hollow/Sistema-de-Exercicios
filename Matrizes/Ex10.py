import numpy as np

linhas = int(input("Digite o número de linhas (M): "))
colunas = int(input("Digite o número de colunas (N): "))
valores = []
print("\nDigite os valores da matriz:")
for i in range(linhas):
    for j in range(colunas):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        valores.append(valor)
matriz = np.array(valores).reshape(linhas, colunas)
print("\nMatriz original:")
print(matriz)
transposta = matriz.T
print("\nMatriz transposta:")
print(transposta)