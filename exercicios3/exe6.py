nome = input("Digite o nome do estudante")
conceito = input("Digite o conceito do estudante (A, B, C ou D")

if(conceito == "A"):
    print("Fortemente recomendado")
else:
    if(conceito == "B" or conceito == "C"):
        print("Recomendado")
    else:
        if(conceito == "D"):
            print("Não recomendado")

