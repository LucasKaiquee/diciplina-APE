num = int(input("Digite o número:"))

maior = 0
menor = 0
num = int(input("Digite um número:"))

while num != 0:
    num = int(input("Digite um número"))
    if num > maior:
        maior = num
    if num < menor:
        menor = num 
print(f"O maior número é {maior} e o menor número é {menor}")

