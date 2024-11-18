def calcula_4op():
    print('calculadora com 4 operações')
    num0 = float(input('insira um numero\n'))
    num1 = float(input('insira outro numero\n'))
    operacoes = ['somar', 'subtrair', 'multiplicar', 'dividir']
    escolha = 4
    saida = 'nao'
    menu = ''
    while saida != 'sim':
        print("Qual dessas operações você deseja fazer?", operacoes)
        escolha = int(input(
            'insira zero para somar, 1 para subtrair, 2 para multiplicar e 3 para dividir\n'))
        menu = operacoes[escolha]
        if menu == 'somar':
            print(f'O valor da soma de {num0}+{num1} é {num0+num1}')
        if menu == 'subtrair':
            print(f'O valor da subtração de {num0}-{num1} é {num0-num1}')
        if menu == 'multiplicar':
            print(f'O valor da multiplcação de {num0}*{num1} é {num0*num1}')
        if menu == 'dividir':
            print(f'O valor da divisão de {num0}/{num1} é {num0/num1}')
        saida = str(input('parar sim ou nao?')).lower()
        escolha = 4
    print('fim da calculadora')


calcula_4op()
