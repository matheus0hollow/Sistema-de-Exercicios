lista = [1, 2, 3, 4, 5]
n = int(input("Digite o número de posições: "))
n = n % len(lista)
lista_rotacionada = lista[-n:] + lista[:-n]
print("Lista rotacionada:", lista_rotacionada)
print(lista)