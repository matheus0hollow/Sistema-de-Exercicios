def rotacionar_90(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    for i in range(n):
        matriz[i].reverse()
    return matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print("Original:")
for linha in matriz:
    print(linha)
rotacionada = rotacionar_90(matriz)
print("\nRotacionada 90°:")
for linha in rotacionada:
    print(linha)