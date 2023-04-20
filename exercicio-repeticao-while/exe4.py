matricula = int(input("Digite a matricula do aluno"))

while matricula != 0:
    nome = input("Digite o nome do aluno:")
    nota1 = float(input("Digite a primeira nota do aluno"))
    nota2 = float(input("Digite a nota do aluno"))

    media = (nota1 + nota2) /2

    if media >= 7:
        print(f"O aluno: {nome}, matricula: {matricula}, está aprovado com média {media}")
    else:
        print(f"O aluno: {nome}, matricula: {matricula}, está reprovado com média {media}")
    matricula = int(input("Digite a matricula do aluno"))