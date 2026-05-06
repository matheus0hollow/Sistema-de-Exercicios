lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 6, 7, 8, 9, 10]
interc = []
for i in lista1:
    if i in lista2:
        interc.append(i)
print(interc)