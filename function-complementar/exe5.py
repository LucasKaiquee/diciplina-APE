def fatorial(valor):
    fat=1
    for i in range(2, valor + 1):
        fat*=i
    return fat

def pontencia(base, expoente):
    return base ** expoente

def cosseno(x):
    cos = 1
    sinal = -1
    for i in range(2, 40, 2):
        cos += sinal*pontencia(x, i)/fatorial(i)
    return cos

x = int(input("digiote o valor de x"))
print(cosseno(x))