v = [None]*10

for i in range(10):
    v[i] = int(input("Digite o valor"))

for j in range(10):
    if j%2 == 0:
        print(f"Pares: o valor está no indice {j} : {v[j]}")
 
for k in range(10):
    if k%2 != 0:
        print(f"Impares: o valor está no indice {k} : {v[k]}")