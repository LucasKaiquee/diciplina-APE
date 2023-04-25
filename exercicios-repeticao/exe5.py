numero_pessoas = int(input("Digite a quantidade de pessoas"))

homem = 0
mulher = 0

for i in range(numero_pessoas):
    sexo = input("Digite o sexo M ou f").upper()

    if sexo == "M":
        homem += 1 
    elif sexo == "F":
        mulher += 1

percentual_homem = homem / numero_pessoas
percentual_mulher = mulher / numero_pessoas

print(f"{percentual_homem * 100:.2f}% Homens e {percentual_mulher * 100:.2f}% Mulheres")