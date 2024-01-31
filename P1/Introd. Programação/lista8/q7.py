str1 = input("Digite um número entre 1 e 99: ")

num = {"1":"um", "2":"dois", "3":"três", "4":"quatro", "5":"cinco", "6":"seis", "7":"sete", "8":"oito", "9":"nove"}
dez = {"10":"dez","11":"onze", "12":"doze", "13":"treze", "14":"quatorze", "15":"quinze", "16":"dezesseis", "17":"dezessete", "18":"dezoito", "19":"dezenove"}
dezenas = {"20":"vinte", "30":"trinta", "40":"quarenta", "50":"cinquenta", "60":"sessenta", "70":"sessenta", "80":"oitenta", "90":"noventa"}

if len(str1) == 1:
    print(f"O número digitado foi: {num[str1]}")
elif len(str1) == 2:
    if int(str1) < 20:
        print(f"O número digitado foi: {dez[str1]}")
    else:
        print(f"O número digitado foi: {dezenas[str1[0]+'0']} e {num[str1[1]]}")