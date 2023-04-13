hodometro_antes = float(input("Digite o valor do hodometro antes:"))
hodometro_depois = float(input("Digite o valor do hodometro depois"))
combustivel_gasto = float(input("Digite a quantidade de combustivel gasto:"))
valor_litro = float(input("Digite o valor do litro de combustivel:"))
capacidade =  float(input("DIgite a capacidade do tanque de combustivel:"))

quilometragem = hodometro_depois - hodometro_antes
km_litro = quilometragem/combustivel_gasto
autonomia = capacidade * km_litro
custo = valor_litro * combustivel_gasto 

print(f"A quilometragem rodada foi: {quilometragem} KM")
print(f"O veiculo faz {km_litro} KM/L")
print(f"De tanque cheio o veiculo roda {autonomia} KM")
print(f"O custo tatal da viagem foi de R$ {custo:.2f}")