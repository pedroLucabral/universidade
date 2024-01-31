turno = input("Qual turno voce estuda?\nM (Matutino)\nV (Vespertino)\nN (Noturno)\n").upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor Invalido")