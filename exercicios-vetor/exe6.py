from tkinter import N


n = int(input("Digite o valor de n"))
v = [None]*n
in_v = [None]*n
cont = 0

for i in range(n):
    v[i] = int(input("Digite"))

for j in range(n-1, -1, -1):
    in_v[j] = v[cont]
    cont +=1

#for k in range(n-1, -1, -1):
    #print(k)
 

print(in_v)