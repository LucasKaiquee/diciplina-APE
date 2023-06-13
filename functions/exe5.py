def media(a, b, c):
    med = (a+b+c)/3
    return med

def conceito(media):
    if media >= 8:
        return 'Conceito: A'
    elif media >=5 and media < 8:
        return 'Conceito B'
    else:
        return 'Conceito C'
    
n1 = int(input("Digite a nota 1"))
n2 = int(input("Digite a nota 2"))
n3 = int(input("Digite a nota 3"))

print(f" A média é {media(n1, n2, n3):.2f} logo: {conceito(media(n1, n2, n3))}")