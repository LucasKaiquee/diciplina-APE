n = int(input("Digite o valor de n"))
a = []
b = []
c = []

for i in range(n):
    a.append(int(input(f"digite o {i + 1}° valor de a")))
    b.append(int(input(f"digite o {i + 1}° valor de b")))

for i in range(n):
    c.append(a[i])
    c.append(b[i])

print(c)
