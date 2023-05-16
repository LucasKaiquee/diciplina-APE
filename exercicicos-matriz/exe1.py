from random import randint
q_linha = 2
q_colunas = 3

a = [[None]*q_colunas for i in range(q_linha)]
b = [[None]*q_colunas for i in range(q_linha)]

for i in range(q_linha):
    for j in range(q_colunas):
        a[i][j] = randint(1, 100)
        b[i][j] = randint(1, 100)

c = [[None]*q_colunas for i in range(q_linha)]

for i in range(q_linha):
    for j in range(q_colunas):
        c[i][j] = a[i][j] + b[i][j]

for i in range(q_linha):
    for j in range(q_colunas):
        print(f"{a[i][j]:4}", end="")
    print("")
    
print("")

for i in range(q_linha):
    for j in range(q_colunas):
        print(f"{b[i][j]:4}", end="")
    print("")

print("")

for i in range(q_linha):
    for j in range(q_colunas):
        print(f"{c[i][j]:4}", end="")
    print("")
