nome = input("Digite o nome do estudante")
conceito = input("Digite o conceito do estudante (A, B, C ou D")

if(conceito == "A"):
    print("Fortemente recomendado")
elif(conceito == "B" or conceito == "C"):
    print("Recomendado")
elif(conceito == "D"):
    print("Não recomendado")
else:
    print("Conceiro invalido")

