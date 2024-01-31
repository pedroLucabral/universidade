lower = higher = num = int(input("Digite um número: "))

sum = 0

while num != -1:
    if num > higher:
        higher = num
    if num < lower:
        lower = num
    sum += num
    num = int(input("Digite um número: "))

print(f"Menor valor: {lower}\nMaior valor:{higher}\nSoma dos valores:{sum}")