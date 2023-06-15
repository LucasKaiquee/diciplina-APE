from operator import le
import random

def gera_matriz(linha, coluna):
    matriz = [[None]*coluna for i in range(linha)]

    for i in range(linha):
        for j in range(coluna):
            matriz[i][j] = random.randint(1, 10)
    return matriz


def exibe(m):
    linha = len(m)
    coluna = len(m[0])
    for i in range(linha):
        for j in range(coluna):
            print(f"{m[i][j]:4}", end="")
        print("")

def soma(n1, n2, linha, coluna):
    n3 = [[None]*coluna for i in range(linha)]
    for i in range(linha):
        for j in range(coluna):
            n3[i][j] = n1[i][j] + n2[i][j]
    return n3


l = int(input("valor1"))
c = int(input("valor2"))

matriz_1 = gera_matriz(l, c)
matriz_2 = gera_matriz(l, c)

print("Primeira matriz:")
exibe(matriz_1)
print("Matriz somada:")
matriz_soma = soma(matriz_1, matriz_2, l, c)
print(exibe(matriz_soma))




