deposito = float(input("Digite o valor do deposito inicial: "))
juros_tx = float(input("Digite a taxa de juros: "))

juros_rendimento = 0

for i in range(1, 25):
    deposito += deposito * (juros_tx/100)
    juros_rendimento += deposito * (juros_tx/100)
    print(f"Mês {i}: {deposito}")

