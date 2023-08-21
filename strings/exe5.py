frase = input("").upper()
n = len(frase)

for i in range(n):
    print(f"{frase[i]*(i+1)}")

for i in range(n-2, -1, -1):
    print(i)
    print(f"{frase[i]*(i+1)}")