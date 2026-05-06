lista = [1,2,2,3,4,5,6,7,2,7,1,4,8,8,9,10]
lista2 = []
for i in lista:
    if i not in lista2:
        lista2.append(i)
print(lista2)