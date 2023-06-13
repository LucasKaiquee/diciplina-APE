def soma(vetor): 
    sum = 0
    for i in range(len(vetor)):
        sum += vetor[i]
    return sum

n = int(input("Digite o tamanho do vetor"))
v = [None]*n

for i in range(len(v)):
    v[i] = int(input("Digite um valor"))


t = [6, 3, 8, 7, 2, 5]

print(soma(v))
print(soma(t))
    