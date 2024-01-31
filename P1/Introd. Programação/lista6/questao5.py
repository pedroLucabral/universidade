num_eleitores = int(input("Digite a quantidade de eleitores: "))

candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range(num_eleitores):
    voto = int(input("Digite seu voto\nOpcoes validas: 13, 22, 12.\n:  "))
    if voto == 13:
        candidato1 += 1
    elif voto == 22:
        candidato2 += 1
    elif voto == 12:
        candidato3 += 1

print(f"Candidato 1: {candidato1}\nCandidato 2: {candidato2}\nCandidato 3: {candidato3}")

