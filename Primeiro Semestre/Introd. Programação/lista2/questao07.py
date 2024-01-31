valor = float(input("Digite o valor da compra: "))
metodo_pgmt = input("Digite o metodo de pagamento: ").lower()

if metodo_pgmt == "dinheiro":
    if valor >= 100:
        print(f"Valor total: {valor-(valor*0.1)}")
    else:
        print(f"Valor total: {valor}")
elif metodo_pgmt == "cheque":
    print(f"Valor total: {valor}")
else:
    print("Forma de pagamento invalida")