contador = 0
soma = 0

while contador < 500:
    if contador %2 != 0 and contador %3 == 0:
        soma += contador
        print(contador)
    contador += 1
print(soma)