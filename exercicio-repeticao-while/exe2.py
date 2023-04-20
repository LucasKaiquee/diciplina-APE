from statistics import median


FLAG = 999
soma = contador = 0

num= int(input("Digite um número:"))
while num != FLAG:
    soma += num
    contador += 1 
    num = int(input("Digite um núemro"))
print(f"A média é: {soma/contador:.2f}")