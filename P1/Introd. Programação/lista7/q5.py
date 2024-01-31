pessoas = [189, "M", 171, "M", 155, "F", 161, "F", 171, "F", 175, "M", 169, "F", 165, "M", 178, "M", 165, "F"]

sexo = []
altura = []

totalPessoas = int(len(pessoas) / 2)

for i in range(0, len(pessoas), 2):
    altura.append(pessoas[i])
    sexo.append(pessoas[i+1])

menorAltura = 500
menorAlturaSexo = ''
maiorAltura = 0
maiorAlturaSexo = ''

for i in range(totalPessoas):
    if altura[i] > maiorAltura:
        maiorAltura = altura[i]
        maiorAlturaSexo = sexo[i]
    if altura[i] < menorAltura:
        menorAltura = altura[i]
        menorAlturaSexo = sexo[i]
    
print(f"Individuo de menor altura tem {menorAltura}cm e é do sexo {menorAlturaSexo}")
print(f"Individuo de maior altura tem {maiorAltura}cm e é do sexo {maiorAlturaSexo}")

totalFeminino = 0
mediaFeminino = 0

totalMasculino = 0
mediaMasculino = 0

for i in range(totalPessoas):
    if sexo[i] == "F":
        mediaFeminino += altura[i]
        totalFeminino += 1
    if sexo[i] == "M":
        mediaMasculino += altura[i]
        totalMasculino += 1

mediaFeminino = mediaFeminino / totalFeminino
mediaMasculino = mediaMasculino / totalMasculino

print(f"A media de altura feminina é: {mediaFeminino}")
print(f"A media de altura masculina é: {mediaMasculino}")

print(f"Total de individuos do sexo feminino: {totalFeminino}")
print(f"Total de individuos do sexo masculino: {totalMasculino}")


    