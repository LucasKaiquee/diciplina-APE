peso = float(input("Digite seu peso"))
altura = float(input("Digite sua altura"))

imc = peso/ (altura *altura)

if(imc < 18.5):
    print("Baixo peso")
elif(imc >= 18.5 and imc >= 25):
    print("Normal")
elif(imc >= 25 and imc < 30):
    print("Sobrepeso")
else:
    print("Obesidade")