quantidade = int(input("Digite um número"))

soma = 0

for i in range(quantidade): 
    valor = int(input(f"Digite o {i + 1}°"))
    soma += valor

print(soma)