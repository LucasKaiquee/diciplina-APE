n = int(input("Digite o valor de n"))

anterior = 0
proximo = 1

print(anterior)
print(proximo)

for i in range(3, n+1):
    soma = anterior + proximo
    print(soma)
    anterior = proximo
    proximo = soma