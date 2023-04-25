n = int(input("Digite um número:"))

maior = 0

for i in range(1, n + 1):
    raiz = i**(1/2)
    if raiz == int(raiz) and i > maior:
        maior = i

print(f"O maior quadrado perfeito é {maior}")