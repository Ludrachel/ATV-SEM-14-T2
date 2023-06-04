num = []
num_negativos = 0
num_positivos = 0

for i in range(10):
    numero = int(input())
    num.append(numero)
    if numero < 0:
        num_negativos += 1
    elif numero > 0:
        num_positivos += numero
print(num)
print(num_negativos)
print(num_positivos)
