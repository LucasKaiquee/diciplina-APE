n = int(input("Digite o valor de n"))
v = [None]*n
cont_par = 0
cont_impar = 0

for i in range(n):
    v[i] = int(input("Digite"))

for i in range(n):
    if v[i] %2 == 0:
        cont_par +=1 
    else:
        cont_impar += 1

    soma = sum(v)
    media = soma/2

print(f"{cont_par}: pares, {cont_impar}: impares, a soma é: {soma}, a média é: {media}")