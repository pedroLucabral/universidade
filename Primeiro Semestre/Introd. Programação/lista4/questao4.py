num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

quociente = 0

while num1 >= num2:
    num1 -= num2
    quociente += 1

print(f"Quociente: {quociente} Resto da divisão: {num1}")