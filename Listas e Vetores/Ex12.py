lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maior = lista[0]
menor = lista[0]
for i in lista:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i
print("o maior numero é ",maior," e o menor é ",menor)
