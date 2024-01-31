import random as r

n = int(input("Digite a quantidade de rolagens do dado: "))
dados = []

if n == 0:
    exit()
for i in range(n):
    dados.append(r.randint(1, 6))

percent = 100 / n

cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0

for i in dados:
    if i == 1:
        cont1 += percent
    if i == 2:
        cont2 += percent
    if i == 3:
        cont3 += percent
    if i == 4:
        cont4 += percent
    if i == 5:
        cont5 += percent
    if i == 6:
        cont6 += percent

print(f"1 ={cont1:.2f}% | 2 = {cont2:.2f}% | 3 = {cont3:.2f}% | 4 = {cont4:.2f}% | 5 = {cont5:.2f}% | 6 = {cont6:.2f}%")