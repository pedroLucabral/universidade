matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz[0][1], matriz[1][0] = matriz [1][0], matriz[0][1]
matriz[1][2], matriz[2][1] = matriz[2][1], matriz[1][2]

for i in matriz:
    print(i)