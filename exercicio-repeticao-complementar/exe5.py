indica_maior = 0
indica_menor = 0
maior = 0
menor = 999

for i in range(1, 5):
    temperatura = int(input("sdgs"))
    if temperatura > maior:
        maior = temperatura
        indica_maior = i
    if temperatura < menor: 
        menor = temperatura
        indica_menor = i

print(f"{indica_maior}: {maior}")
print(f"{indica_menor}: {menor}")