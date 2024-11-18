def conta_caracter():
    frase = str(input("Insira uma frase: "))
    contador = {}

    for c in frase:
        if c in contador:
            contador[c] += 1
        else:
            contador[c] = 1

    print('Contagem de cada caractere:', contador)


conta_caracter()
