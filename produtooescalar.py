lista_1 = []
lista_2 = []

for x in range(5):
    num_1 = int(float(input()))
    lista_1.append(num_1)
    
for y in range(5):
    num_2 = int(float(input()))
    lista_2.append(num_2)

produto = 0

for i in range(5):
    produto += lista_1[i] * lista_2[i]

print(lista_1)
print(lista_2)


print(f'({lista_1[0]} x {lista_2[0]}) + ({lista_1[1]} x {lista_2[1]}) + ({lista_1[2]} x {lista_2[2]}) + ({lista_1[3]} x {lista_2[3]}) + ({lista_1[4]} x {lista_2[4]}) = {produto}')
