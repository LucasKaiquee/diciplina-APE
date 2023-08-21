from tkinter import N

def vetor(n=20):
    vetor = [None]*n
    for i in range(n):
        vetor[i] = int(input("Digite um valor"))

    return vetor

def media(v):
    media = soma = 0
    for i in range(len(v)):
        soma += v[i]
    media = soma/len(v)
    return media

def verifica(v, n):
    cont = 0
    for i in range(len(v)):
        if v[i] < n:
            cont += 1
    return cont


n = int(input('Digite um valor'))
vetor_teste = vetor(n)

print(vetor_teste)
print(media(vetor_teste))

x = int(input("digite o numero para verificar"))
print(verifica(vetor_teste, x))