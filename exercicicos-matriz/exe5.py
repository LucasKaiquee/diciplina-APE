nlinha = 20
ncoluna = 4
media = media_geral = soma = cont = 0
m = [[None]*ncoluna for i in range(nlinha)]

for i in range(nlinha):
    for j in range(ncoluna):
        if j != 3:
            m[i][j] = int(input("Digite a nota"))
            soma += m[i][j]
            media = soma / 3
        elif j == 3:
            m[i][j] = media
    soma = media = 0

soma = media = 0
for i in range(nlinha):
    for j in range(ncoluna):
        print(f"{m[i][j]:6.1f}", end="")
    print("")

for i in range(nlinha):
    soma += m[i][ncoluna-1]
    media_geral = soma/nlinha

    if m[i][ncoluna-1] > media_geral:
        cont += 1

print(f"a media geral é: {media_geral:.2f}, {cont} alunos acima da média")