while True:
    nome = input("nome")
    entrada = int(input("ano que entrou"))
    ano_n = int(input("Ano de nascimento"))

    tempo = 2021 - entrada
    idade = 2021 - ano_n

    if idade >= 65 or tempo >= 30:
        print(f"{nome}, {idade}, {tempo}, pode")
    elif idade >= 30 and tempo >= 25:
        print(f"{nome}, {idade}, {tempo}, pode")
    else:
        print("não pode")
        
    cont = input("deseja continuar s ou n").lower()
    if cont == "n":
        break