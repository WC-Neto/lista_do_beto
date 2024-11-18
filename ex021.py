def lista_sem_repetidos():
    print('lista sem repetidos e na mesma ordem inicial')
    numeros = [10, 7, 5, 23, 7, 24, 10]
    novalista = []
    for i in numeros:
        if i not in novalista:
            novalista.append(i)
    print(novalista)


lista_sem_repetidos()
