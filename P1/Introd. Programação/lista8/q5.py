str1 = input("Digite sua frase: ")

def ocorrencias(char, string):
    cont = 0
    for i in string:
        if i.lower() == char.lower():
            cont += 1
    return cont

contagem = {}

for i in str1:
    if i not in contagem:
        contagem[i] = ocorrencias(i, str1)

print(contagem)