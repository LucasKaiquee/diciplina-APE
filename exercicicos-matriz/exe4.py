from random import randint

nlinha = 3
ncoluna = 5

m = [[None]*ncoluna for i in range(nlinha)]
mt = [[None]*nlinha for i in range(ncoluna)]

for i in range(nlinha):
    for j in range(ncoluna):
        m[i][j] = randint(-9, 9)

for i in range(nlinha):
    for j in range(ncoluna):
        mt[j][i] = m[i][j]

for i in range(nlinha):
    for j in range(ncoluna):
        print(f"{m[i][j]:4}", end="")
    print("")

print("")

for i in range(ncoluna):
    for j in range(nlinha):
        print(f"{mt[i][j]:4}", end="")
    print("")