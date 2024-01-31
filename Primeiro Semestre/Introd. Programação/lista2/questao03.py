salario_hora = float(input("Quanto voce ganha por hora?\n"))
horas_trabalhadas = int(input("Quantas horas voce trabalhou em um mes?\n"))

salario_bruto = salario_hora*horas_trabalhadas
desconto_ir = salario_bruto*(11/100)
desconto_inss = salario_bruto*(8/100)
desconto_sind = salario_bruto*(5/100)

print(f"Salario Bruto: R${salario_bruto}")
print(f"Desconto Imposto de Renda: R${desconto_ir}")
print(f"Desconto INSS: R${desconto_inss}")
print(f"Desconto Sindicato: R${desconto_sind}")
print(f"Salario Liquido: R${salario_bruto-desconto_ir-desconto_inss-desconto_sind}")