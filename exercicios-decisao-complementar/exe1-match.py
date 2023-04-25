dia = int(input("Digite o número referente ao dia da semana:"))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("O número deve estar entre 1 e 7")

if(dia == 1 or dia == 7):
    print("Final de semana")
else:
    print("Dia útil")