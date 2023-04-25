PESO_N1 = 6
PESO_N2 = 4

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite o valor da segundo nota"))

media = ((n1 * PESO_N1) + (n2 * PESO_N2)) / PESO_N1 + PESO_N2

print(f"A média do aluno será:, {media:.1f}")
