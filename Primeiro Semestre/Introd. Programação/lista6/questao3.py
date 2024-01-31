pessoa_num = int(input("Digite a quantidade de pessoas: "))
soma = 0

for i in range(1, pessoa_num+1):
    soma += int(input(f"Digite a idade da {i}° pessoa: "))

media = soma/pessoa_num
if 0 < media <= 25:
    print("A turma é jovem")
elif media <= 60:
    print("A turma é adulta")
else:
    print("A turam é idosa.")