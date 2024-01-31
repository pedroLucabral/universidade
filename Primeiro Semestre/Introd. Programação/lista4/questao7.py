n = int(input("Digite um número: "))

b = 2
p =((b+(n/b)) /2)

while abs(p-b) > 0.0001:
    b = p
    p =((b+(n/b)) /2)

print(p)