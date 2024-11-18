def contador_de_numeros():
    print('Contador de números em uma lista\n')
    continuar = True
    lista = []
    contador = 1
    while continuar != False:
        lista.append(int(input('insira um número\n')))
        continuar = str(input('Deseja continuar?S para sim ou N para não\n'))
        if continuar in 'Nn':
            continuar = False
        else:
            continuar = True
            contador += 1
    print(f'A lista contém {contador} número(s)')


contador_de_numeros()
