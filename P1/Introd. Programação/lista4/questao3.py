paisX = 70000
paisY = 180000
anos = 0

while paisX < paisY:
    paisX += int(paisX * (3.5/100))
    paisY += int(paisY * (1.5/100))
    anos += 1
    print(f"X:{paisX} | Y: {paisY} | Ano: {anos}")

print("\n============================================\n")
print(f"A população do país X ultrapassou a do país Y em {anos} anos.\n")