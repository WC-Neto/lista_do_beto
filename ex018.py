def soma_matriz_quadrada():
    print('soma de matriz quadrada')
    matriz = [0, 0], [0, 0]
    # l = line, c = column
    for l in range(0, 2):
        for c in range(0, 2):
            matriz[l][c] = int(input())
    principal = matriz[1][1] + matriz[0][0]
    secundaria = matriz[0][1] + matriz[1][0]
    for l in range(0, 2):
        for c in range(0, 2):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()
    print(f' A soma da principal é {principal} e a secundaria é {secundaria}')


soma_matriz_quadrada()
