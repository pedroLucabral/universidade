n = int(input("Digite um número: "))

ult = 1
penult = 0

for i in range(1, n+1):
    num = ult + penult
    print(num)
    penult, ult = ult, penult + ult
    ult = num

    
