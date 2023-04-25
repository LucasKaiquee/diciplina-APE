BIT_50 = 50
BIT_10 = 10
BIT_5 = 5
BIT_1 = 1

valor = int(input("Digite a quantidade de bits"))

nota_50 = valor // BIT_50
resto1 = valor % BIT_50

nota_10 = resto1 // BIT_10
resto2 = resto1 % BIT_10

nota_5 = resto2 // BIT_5
resto3 = resto2 % BIT_5

nota_1 = resto3 // BIT_1

print(f"Troco: {nota_50} notas de B$ 50, {nota_10} notas de B$ 10, {nota_5} notas de B$ 5, {nota_1} notas de B$ 1")



