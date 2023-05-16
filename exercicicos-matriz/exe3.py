from random import randint

n = int(input("Digite a ordem da matriz quadrado"))
a = [[None]*n for i in range(n)]
b = [[None]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = randint(1, 9)

for i in range(n):
    for j in range(n):
        if i == j or j == n-1-i:
            b[i][j] = 0
        else:
            b[i][j] = i + j + a[i][j]

for i in range(n):
    for j in range(n):
        print(f"{a[i][j]:4}", end="")
    print("")

print("")
for i in range(n):
    for j in range(n):
        print(f"{b[i][j]:4}", end="")
    print("")

    

