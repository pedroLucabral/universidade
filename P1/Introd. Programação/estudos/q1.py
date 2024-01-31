numero = input("Digite seu número: ")

#1234-5678

if numero[4] == "-" and len(numero) == 9:
   novo_num = numero
elif numero[3] == "-" and len(numero) == 8:
    novo_num = "3" + numero 
elif len(numero) == 8:
    novo_num = numero[:4] + "-" + numero[4:] 
else:
    novo_num = "3" + numero
    novo_num = novo_num[:4] + "-" + novo_num[4:]

print(novo_num)