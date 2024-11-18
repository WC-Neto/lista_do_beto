def palindromo():
    frase = str(input('insira uma palavra\n'))
    print(frase[::-1])
    if frase in frase[::-1]:
        print('é palindromo')
    else:
        print('não é palindromo')


palindromo()
