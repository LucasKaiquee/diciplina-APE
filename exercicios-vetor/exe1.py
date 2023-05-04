n = int(input("Digite o valor de n"))
k = int(input("Digite o valor de k"))
a = [None]*n
b = [None]*n

for i in range(n):
    a[i] = int(input("Digite"))
    b[i] = a[i] *k

print(b)
