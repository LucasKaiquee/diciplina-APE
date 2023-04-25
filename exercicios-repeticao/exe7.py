num = int(input("Digite um número"))

if num == 1:
    primo = False 
else:
    primo = True
    for i in range(2, num):
        if(num%i == 0):
            primo = False
if primo:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")

