def numeros_primos():
    print('Números primos entre 10 e 50:')
    numeros = list(range(10, 51))

    for numero in numeros:
        divisivel = 0
        for c in range(1, numero + 1):
            if numero % c == 0:
                divisivel += 1
        if divisivel > 2:
            print(f'{numero} não é primo')
        else:
            print(f'{numero} é primo')


numeros_primos()
