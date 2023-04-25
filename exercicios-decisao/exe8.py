num1 = float(input("Digite primeiro numero"))
num2 = float(input("Digite o segundo numero"))
operador = input("Digite o operador (+, -, *, /, %")

if(operador == "+"):
    print(num1 + num2)
elif(operador == "-"):
    print(num1 - num2)
elif(operador == "*" or operador == "x"):
    print(num1 * num2)
elif(operador == "/"):
    if(num2 !=0):
        print(num1/num2)
    else:
        print("Operação invalida")
elif(operador == "%"):
    print(num1 % num2)
else:
    print("Operador invalido")