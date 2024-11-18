def media():
    print('média aritmética')
    n1 = float(input('Insira sua primeira nota\n'))
    n2 = float(input('Insira sua segunda nota\n'))
    n3 = float(input('Insira sua terceira nota\n'))
    media = (n1 + n2 + n3)/3
    print(f'A sua média com base nas suas notas é {media}')


media()
