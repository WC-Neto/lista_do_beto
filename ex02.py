def pareimpar():
    print('pares e impares!\n')
    num = int(input('Insira o número a ser verificado\n'))
    if num % 2 == 0:
        print(f'{num} é par!')
    else:
        print(f'{num} é impar!')


pareimpar()
