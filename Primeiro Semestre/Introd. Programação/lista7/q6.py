pontos = [(1, 2), (3, 5), (7, 15), (2, 13), (17, 21), (8, 29)]

lista = []

for i in pontos:
    menorDist = 999999999999
    maiorDist = 0
    mediaDist = 0
    for j in pontos:
        if i != j:
            dist = ((j[0] - i[0])**2 + (j[1] - i[1]) **2)**(1/2)
            if dist < menorDist:
                menorDist = dist
            if dist > maiorDist:
                maiorDist = dist
            mediaDist += dist
    lista.append([menorDist, maiorDist, mediaDist/len(pontos)])

for i in range(len(pontos)):
    print(f"Ponto {pontos[i]}:\n Distancia Minima: {lista[i][0]} Distancia Maxima: {lista[i][1]}\n Media de Distancia: {lista[i][2]}")
            