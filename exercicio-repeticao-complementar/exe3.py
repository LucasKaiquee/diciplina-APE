SENHA = "abcd"
cont = 0

while True:
    passe = input("").lower()
    if passe == SENHA:
        print("senha correta")
        break
    else:
        print("Senha incorreta")
        cont += 1
        if cont >= 3:
            break
