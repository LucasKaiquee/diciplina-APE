num1 = float(input("Digite primeiro numero"))
num2 = float(input("Digite o segundo numero"))
operador = input("Digite o operador (+, -, *, /, %")

if(operador == "+"):
    print(num1 + num2)
elif(operador == "-"):
    print(num1 - num2)
elif(operador == "*"):
    print(num1 * num2)
elif(operador == "/"):
    print(num1/num2)
elif(operador == "%"):
    print(num1 % num2)
else:
    print("Operador invalido")