cpf = input("Digite seu cpf (xxx.xxx.xxx-xx): ")

if cpf[3] == "." and cpf [7] == "." and cpf [11] == "-":
    print("CPF Válido")
else:
    print("CPF Inválido")