codigo = input("DIgite o código do lanche (H, C, B, F ou X para fechar)").lower()
valor = 0

while codigo != "x":

    qtd = int(input("Digite a quantidade"))

    match codigo:
        case "h":
            preco = 5
        case "c":
            preco = 6
        case "b":
            preco = 7
        case "f":
            preco = 4

    lanche_total = preco * qtd
    valor += lanche_total

    codigo = input("DIgite o código do lanche (H, C, B, F ou X para fechar)").lower()

print(f"Total a pagar: R$ {valor}.00")