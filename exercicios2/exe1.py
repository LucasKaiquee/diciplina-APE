SALARIO =  1000
COMISSAO = 200
PORCENTAGEM = 5/100

nome = input ("Digite o nome do vendendor:")
carros_vendidos = int(input("Digite o número de carros vendidos:"))
valor_total = float(input("O valor total vendido foi:"))

salario_final = SALARIO + (carros_vendidos * 200) + (valor_total * PORCENTAGEM)

print(f"O salário de {nome} foi de {salario_final}")

