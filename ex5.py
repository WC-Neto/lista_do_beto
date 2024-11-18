def tabuada():
    print('Gerador de tabuada\n')
    x = int(input('Insira o número que deseja saber a taboada\n'))
    for i in range(11):
        print(f' {x} * {i} = {x*i}')
    print('fim da taboada')


tabuada()
