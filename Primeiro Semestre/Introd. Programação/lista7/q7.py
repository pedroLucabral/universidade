frase = input("Digite a frase:\n")
frases = []

while frase != "-1":
    letras = list(frase)
    dic = {}

    for i in letras:
        if i.lower() in dic or i.upper() in dic:
            for j in dic:
                if i.lower() == j or i.upper() == j:
                    dic[j] = dic[j] + 1
                    add = True
                    equal = dic[j]
            if add:
                dic[i] = equal
        else:
            dic[i] = 1
        
    frases.append(dic)

    frase = input("\nDigite a frase: \n")

for i in frases:
    print(i)