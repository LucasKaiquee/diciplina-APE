contador = 0
soma = 0
num = int(input("Digite um número:"))
while contador < 30:
    contador += 1
    soma += num
    num = int(input("Digite um número:"))

print(soma)