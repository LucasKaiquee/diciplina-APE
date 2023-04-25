num = int(input("Digite um número"))
cont = 1

while cont == 1:
    if num%2 == 0:
        print("O número é par")
    else:
        print("O número é impar")
    continuar = input("Deseja continuar ? (s ou n)")
    if continuar == "n":
        cont = 0
    else:
        num = int(input("Digite o número"))