v = []
v.append(int(input(f"Digite o valores distintos")))

for i in range(5):
    if v.count(v[i]) > 1:
        print("O valor já foi inserido")
        v.remove(v[i])
        i-1
    else:
        v.append(int(input(f"Digite o valores distintos")))
       

print(v)