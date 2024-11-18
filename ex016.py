def calculadora_fatorial():
    print('calculadora fatorial')
    numero = int(input())
    fatorial = numero
    while numero != 1:
        fatorial = fatorial * (numero - 1)
        numero -= 1
    print(f'O fatorial do valor que pediu é {fatorial}')


calculadora_fatorial()
