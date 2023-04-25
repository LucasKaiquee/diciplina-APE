nome = input("Digite seu nome")
sexo = input("DIgite seu sexo (M ou F)")

if(sexo == "M"):
    print(f"Ola, Sr. {nome}!")
elif(sexo == "F"):
    print(f"Ola, Sra. {nome}!")
else:
    print("Sexo inválido: escolha M ou F")
    