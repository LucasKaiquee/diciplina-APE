from tkinter import N


n = int(input("Digite o valor de n"))
v = [None]*n
maior = 0
menor = 65000
index_maior = 0
index_menor = 0

for i in range(n):
    v[i] = int(input("Digite"))

for j in range(n):
    if maior < v[j]:
        maior = v[j]
        index_maior = j

for k in range(n):
    if menor > v[k]:
        menor = v[k]
        index_menor = k

print(f"O maior número {maior} na posição {index_maior}, O menor número {menor} na posição {index_menor}")
