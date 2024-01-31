num = int(input("Digite um numero: "))

primo = True

for i in range(num -1, 3, -1):
    if num % i == 0:
        primo = False
        break

print("O numero e primo" if primo == True else "O numero nao e primo")