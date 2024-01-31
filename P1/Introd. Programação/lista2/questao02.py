altura = float(input("Digite sua altura em metros:\n"))
sexo = input("Digite seu sexo biologico (M: Masculino / F:Feminino)\n")

if sexo == "M":
    print(f"Seu peso ideal é {72.7*altura-58:.2f}")
elif sexo == "F":
    print(f"Seu peso ideal e {62.1*altura-44.7:.2f}")