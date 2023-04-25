idade = int(input("Digite a idade:"))

qtd_idade = 0
soma_idade = 0
maior_18_21 = 0
menor = 999

while idade != 0:
    soma_idade += idade
    qtd_idade += 1
    idade = int(input("Digite a idade"))

    if idade >= 18 and idade <= 21:
        maior_18_21 += 1
    
    if idade < menor and idade != 0:
        menor = idade

print(f"A média das idades é: {soma_idade/qtd_idade:.2f}")
print(f"A porcetagem de pessoas entre 18 e 21 anos é: {(maior_18_21/qtd_idade)*100:.2f}%")
print("A menor idade é: ",menor)
    