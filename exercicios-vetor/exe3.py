from tkinter import N
from tokenize import Number


n = int(input("Digite o valor de n"))
k = 0
v = [None]*n

for i in range(n):
    v[i] = int(input("Digite"))

k = int(input("Digite o valor de k"))
for j in range(n):
    if v[j] == k:
        print(f"o valor {k} apareceu no index: {j}")
    
    



