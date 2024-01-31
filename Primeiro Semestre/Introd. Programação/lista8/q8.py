import random as r

palavras = ["dromedario", "maracuja", "espeto", "dinossauro", "fantastico"]

segredo = r.choice(palavras)
espaços = ["_" for i in range(len(segredo))]
tentativas = []

total = 6

fim = False
for i in espaços:
    print(i, end=" ")
print("\n")
while fim == False:
    contador = -1
    letra = input("Digite uma letra: ")
    if letra in segredo:
        tentativas.append(letra)
        for i in segredo:
            contador += 1
            if letra == i:
                espaços[contador] = letra
        for i in espaços:
            print(i, end=" ")
        print("\n")
    else:
        total -= 1
        print(f"Não foi dessa vez! Você ainda pode errar {total} vezes.")
    
    if total == 0:
        print(f"Você perdeu! A palavra era {segredo}")

    digitada = ""
    for i in espaços:
        digitada += i
    if digitada == segredo:
        print("Você ganhou!")
        fim = True
    



