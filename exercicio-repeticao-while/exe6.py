CHICO = 1.50
ZE = 1.10
cont = 0 
while CHICO > ZE:
    CHICO += 0.02
    ZE += 0.03
    cont += 1

print(f"Zé demorou {cont} anos para ficar da altura de Chico")