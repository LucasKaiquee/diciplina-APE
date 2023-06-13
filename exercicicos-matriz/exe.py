from random import randint

gabarito = [None]*50
cont = 0

for i in range(50):
    gabarito[i] = randint(1,5)

aluno = 0
while aluno < 30:
    cont = 0
    prova = [None]*50
    for j in range(50):
        prova[j] = randint(1,5)
        if prova[j] == gabarito[j]:
            cont += 2
    print(f"O aluno {aluno + 1} teve nota: {cont}")
    aluno += 1