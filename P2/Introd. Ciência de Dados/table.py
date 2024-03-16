#Pedro Lucas Simões Cabral
#Matricula: 20230014238

from tabulate import tabulate
from statistics import mean
from copy import deepcopy
import csv

def createTable(columns, valuesMatrix):
    
    tableObj = {}

    for i in columns:
        tableObj[i] = []

    if len(valuesMatrix[0]) > len(columns):
        raise Exception("The number of values on the matrix exceeds the amount of columns on the table")

    print(len(valuesMatrix[0]))
    for i in range(len(columns)):
        for j in range(len(valuesMatrix)):
            tableObj[columns[i]].append(valuesMatrix[j][i])

    return tableObj

def addRow(table, valuesList):
    tableObj = deepcopy(table)
    if len(valuesList) > len(tableObj):
        raise Exception("The number of values on the list exceeds the size of the table")
    
    for i in range(len(tableObj)):
        tableObj[list(tableObj.keys())[i]].append(valuesList[i])

    return tableObj

def removeRow(table, index):
    tableObj = deepcopy(table)
    if index > len(tableObj[list(tableObj.keys())[0]]):
        raise Exception("The index is out of range")

    for i in range(len(tableObj)):
        tableObj[list(tableObj.keys())[i]].pop(index)

    return tableObj

def addColumn(table, columnName, valuesList):
    tableObj = deepcopy(table)
    if columnName in list(tableObj.keys()):
        raise Exception("The column already exists")
    
    if len(valuesList) > len(tableObj[list(tableObj.keys())[0]]):
        raise Exception("The number of values on the list exceeds the size of the table")

    tableObj[columnName] = valuesList

    return tableObj

def removeColumn(table, columnName):
    tableObj = deepcopy(table)
    if columnName not in list(tableObj.keys()):
        raise Exception("The column does not exist")

    tableObj.pop(columnName)

    return tableObj

def sumColumns(table):
    tableObj = deepcopy(table)
    allSums = {}
    for i in list(tableObj.keys()):
        intValues = 0
        hasInt = 0
        for j in tableObj[i]:
            if type(j) == int or type(j) == float:
                hasInt = 1
                intValues += j
        if hasInt == 1:
            allSums[i] = intValues
        
    return allSums

def meanColumns(table):
    tableObj = deepcopy(table)
    allSums = {}
    for i in list(tableObj.keys()):
        intValues = []
        hasInt = 0
        for j in tableObj[i]:
            if type(j) == int or type(j) == float:
                hasInt = 1
                intValues.append(j)
        if hasInt == 1:
            allSums[i] = mean(intValues)
        
    return allSums

def printTable(tableObj):
    print(tabulate(tableObj, headers="keys", tablefmt="fancy_grid"))


def readCsv(file):
    tableObj = {}

    with open(file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for i in reader.fieldnames:
            tableObj[i] = []
    
        for column in reader:
            for i in column:
                tableObj[i].append(column[i])

    return tableObj

def filter(table, filterFunction):
    tableObj = deepcopy(table)
    allRows = [[] for i in range(len(tableObj[list(tableObj.keys())[0]]))]

    for i in range(len(tableObj[list(tableObj.keys())[0]])):
        for j in range(len(tableObj)):
            allRows[i].append(tableObj[list(tableObj.keys())[j]][i])

    filtered = []
    for i in allRows:
        if filterFunction(i):
            filtered.append(allRows.index(i))

    for i in range(len(tableObj[list(tableObj.keys())[0]])-1, -1, -1):
        if i not in filtered:
            tableObj = removeRow(tableObj, i)
    
    return tableObj