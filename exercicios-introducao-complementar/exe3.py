valor1 = int(input("Digite o primeiro valor"))
valor2 = int(input("Digite o segundo valor"))

print(f"O valor lido primeiro é: {valor1}, o segundo valor lido é: {valor2}")

x = valor1
valor1 = valor2
valor2 = x

print(f"Após a troca: O valor lido primeiro é: {valor1}, o segundo valor lido é: {valor2}")
