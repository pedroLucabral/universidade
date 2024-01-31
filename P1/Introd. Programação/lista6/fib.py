n = int(input("Digite a quantidade de números da sequência de Fibonacci que deseja gerar: "))
a, b = 0, 1
n1_f = [a, b]

for i in range(2, n):
    a, b = b, a + b
    n1_f += [b]

print("Lista de Fibonacci com", n, "números:")
print(n1_f)