lado1 = int(input("Digite o lado 1"))
lado2 = int(input("Digite o lado 2"))
lado3 = int(input("Digite o lado 3"))

if(lado1 == lado2 == lado3):
    print("Triangulo equilatero")
elif(lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print("Triangulo Isósceles")
else:
    print("Tringulo escaleno")