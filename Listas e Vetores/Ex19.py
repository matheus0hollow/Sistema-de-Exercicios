lista = [3, -2, 5, -1, 6, -3]
max_atual = lista[0]
max_global = lista[0]
for i in range(1, len(lista)):
    max_atual = max(lista[i], max_atual + lista[i])
    max_global = max(max_global, max_atual)
print("Maior soma de sublista:", max_global)