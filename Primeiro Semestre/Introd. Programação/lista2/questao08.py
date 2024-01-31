valor = float(input("Digite o valor da compra: "))
metodo_pgmt = input("Digite o metodo de pagamento: ").lower()

if metodo_pgmt == "dinheiro":
    if valor >= 100:
        print(f"Valor total: R${valor-(valor*0.1)}")
    else:
        print(f"Valor total: R${valor}")
elif metodo_pgmt == "cheque":
    print(f"Valor total: R${valor}")
elif metodo_pgmt == "cartao":
    debt_or_credit = input("Digite se quer pagar com credito ou debito: ").lower()
    if debt_or_credit == "credito":
        parcelas = int(input("Em quantas vezes deseja dividir? (Limite de 3)"))
        if parcelas > 1 and parcelas < 4:
            print(f"Valor total: R${valor}\n{parcelas} parcela(s) de {valor/parcelas}")
        elif parcelas > 3:
            print("Quantidade de parcelas invalida")
        else:
            print(f"Valor total: R${valor}")
    elif debt_or_credit == "debito":
            print(f"Valor total: {valor}")
else:
    print("Forma de pagamento invalida")