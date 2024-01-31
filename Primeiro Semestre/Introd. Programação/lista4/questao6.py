codigo = int(input("Digite o código do produto: "))
#qtd = int(input("Digite a quantidade: "))

valor_total = 0.0

while codigo != 0:
    qtd = int(input("Digite a quantidade: "))
    if codigo == 1:
        valor_total += 5.50 * qtd
    elif codigo == 2:
        valor_total += 2.30 * qtd
    elif codigo == 3:
        valor_total += 4.75 * qtd
    elif codigo == 4:
        valor_total += 6.80 * qtd
    elif codigo == 5:
        valor_total += 9.30 * qtd
    else:
        print("Código Inválido.")
    codigo = int(input("Digite o código do produto: "))
    

print(f"Valor total das compras: {valor_total}")
