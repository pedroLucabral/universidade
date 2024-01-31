valor_total = float(input("Digite o valor inicial da divida: "))
juros = float(input("Digite o juro mensal: "))
parcela = float(input("Qual o valor pago mensalmente: "))


valor_pago = 0.0
juros_pago = 0.0
mes = 0

while valor_pago < valor_total:
    juros_pago += juros
    valor_pago += parcela
    mes += 1

print(f"Valor pago: {valor_pago}")
print(f"Juros Pagos: {juros_pago}")
print(f"A divida será paga em {mes} meses")