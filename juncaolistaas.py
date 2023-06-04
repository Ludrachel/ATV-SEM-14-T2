lista_1 = []
lista_2 = []
for i in range(10):

    n1 = int(input())
    if n1 not in lista_1:
        lista_1.append(n1)

for k in range (10):

    n2 = int(input())
    if n2 not in lista_2:
        lista_2.append(n2)

lista_3 = lista_1.copy()

for n in lista_2:
    if n not in lista_3:

        lista_3.append(n)

print(lista_3)



