n = int(input("Digite um número "))
maior = 0

for i in range(n):
    teste = i**(1/2)
    if maior < i:
        maior = i
        if teste**2 == i:
            print(f"O {maior} é o quadrado perfeito mais proximo de {n}")
