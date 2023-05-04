v = [None]*5

for i in range(5):
    v[i] = int(input("Digite o valor"))

for j in range(5):
    if j%2 == 0:
        print(f"Pares: o valor está no indice {j} : {v[j]}")
 
for k in range(5):
    if k%2 != 0:
        print(f"Impares: o valor está no indice {k} : {v[k]}")