k = int(input("Digite o valor de k"))
v = [None]*5
cont = 0
for i in range(5):
    v[i] = int(input("Digite"))
    if v[i] == k:
        cont += 1

print(f"{k} apareceu {cont}")
