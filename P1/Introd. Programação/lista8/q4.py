str1 = input("Digite sua frase: ")

str2 = ""

for i in str1:
    if i != " ":
        str2 = str2 + i

print(str2)