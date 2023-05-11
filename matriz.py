import mailbox
from random import randint, random


from random import randint

q_linhas = int(input("Digite quantas linhas"))
q_colunas = int(input("Digite quantas colunas"))

matriz = [[None]*q_colunas for i in range(q_linhas)]

for i in range(q_linhas):
    for j in range(q_colunas):
        matriz[i][j] = randint(1, 20)

for i in range(q_linhas):
    for j in range(q_colunas):
        print(f"{matriz[i][j]:4}", end="")
    print()

maior = matriz[0][0]
for i in range(q_linhas):
    for j in range(q_colunas):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

cont = 0

for i in range(q_linhas):
    for j in range(q_colunas):
        if matriz[i][j] == maior:
            cont += 1
            print(f"se repete na posição: {i}x{j}", end="")

print(f"O maior número se repitiu {cont}")
