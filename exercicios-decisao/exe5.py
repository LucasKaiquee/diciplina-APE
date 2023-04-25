from calendar import c


SALARIO_MINIMO = 1320
COMISSAO = 0.05

vendas = float(input("Digite o valor total das vendas"))

salrio_final = vendas * COMISSAO


if(salrio_final >= SALARIO_MINIMO): 
    print(f"O salario é {salrio_final + SALARIO_MINIMO}")
else:
    print("O salario não pode ser inferior ao salrio minimo")
