from random import randint

n = int(input("Digite a ordem da matriz quadrado"))
m = [[None]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        m[i][j] = randint(1, 100)
    
for i in range(n):
    for j in range(n):
        print(f"{m[i][j]:4}", end="")
    print("")
    
print("")

for i in range(n):
    for j in range(n):
        m[i][j] = 0
        print(f"{m[i][j]:4}", end="")
        if i == j:
            print(m[i][j], end=" ")
        print("")