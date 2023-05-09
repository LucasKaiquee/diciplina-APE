v = []

for i in range(6):
    v.append(int(input("Digite")))

for i in range(6):
    cont = v.count(v[i])
    if cont > 1:
        des = "Não é destinto"
    else:
        des = "é destinto"

print(f"O vetor {des}")