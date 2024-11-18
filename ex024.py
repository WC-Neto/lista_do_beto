def anagrama():
    nome1 = str(input('insira primeira palavra\n'))
    nome2 = str(input('insira segunda palavra\n'))
    nome1 = sorted(nome1)
    print(nome1)
    nome2 = sorted(nome2)
    print(nome2)
    if nome1 == nome2:
        print('é um anagrama')
    else:
        print('não é um anagrama')


anagrama()
