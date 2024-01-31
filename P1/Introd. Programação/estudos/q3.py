lista1 = []

for i in range(5):
    n = int(input("Digite um número: "))
    lista1.append(n)

lista2 = []

for i in lista1:
    if i % 2 == 0:
        lista2.append(i)

print(lista2)