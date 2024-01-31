nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media > 9:
    print("A")
elif media > 7.5:
    print("B")
elif media > 6:
    print("C")
elif media > 4:
    print("D")
else:
    print("E")
