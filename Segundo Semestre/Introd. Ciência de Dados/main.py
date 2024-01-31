from table import *

#Definindo a lista de nomes e a matriz de valores
nomesColunas = ["Nome", "Idade", "Curso", "Rank"]

valoresMatriz = [
                    ["Pedro", 18, "CDIA", 1],
                    ["Wesley", 20, "CDIA", 2],
                    ["Julia", 19, "CDIA", 3],
                    ["Carlos", 20, "CDIA", 4],
                    ["Gabriele", 19, "CDIA", 5],
                    ["Gabriel", 20, "CC", 6],
                    ["Lucas", 20, "CC", 7]
                ]

#Criando a tabela
table1 = createTable(nomesColunas, valoresMatriz)
printTable(table1)
print("Criando a tabela\n\n")


#Adicionando uma linha
table1 = addRow(table1, ["Clarice", 20, "CDIA", 8])
printTable(table1)
print("Adicionando uma linha\n\n")

#Removendo uma linha a partir do indice
table1 = removeRow(table1, 3)
printTable(table1)

print("Removendo uma linha a partir do indice\n\n")

#Removendo uma coluna a partir do nome
table1 = removeColumn(table1, "Rank")
printTable(table1)
print("Removendo uma coluna a partir do nome\n\n")

#Adicionando uma coluna
table1 = addColumn(table1, "Sexo", ["M", "M", "F", "F", "M", "M", "F"])
printTable(table1)
print("Adicionando uma coluna\n\n")

#Soma e média dos valores das colunas que possuem números
print(f"Soma dos valores das colunas que possuem números: {sumColumns(table1)}\n")
print(f"Média dos valores das colunas que possuem números: {meanColumns(table1)}\n\n")

#Criação de tabela a partir de arquivo csv
table2 = readCsv("addresses.csv")
printTable(table2)
print("Criação de tabela a partir de arquivo csv de informações sobre personagens do jogo League of Legends\n\n")

#=====================
#Funções para serem passadas como paramêtro para o filtro
def onlyMales(row):
    return True if row[3] == "M" else False

def onlyCC(row):
    return True if row[2] == "CC" else False
    
def onlyADCarries(row):
    return True if row[1] == "AD Carry" else False

def highAttackRange(row):
    return True if int(row[4]) >= 550 else False
#================================

printTable(filter(table1, onlyMales))
printTable(filter(table1, onlyCC))

printTable(filter(table2, onlyADCarries))
printTable(filter(table2, highAttackRange))