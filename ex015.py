def jogo_de_adivinhacao():
    from random import randint
    print('jogo de adivinhação')
    numero = 0
    target = randint(0, 101)
    while numero != target:
        numero = int(input())
        if numero > target:
            print('numero inserido é maior que o que estou pensando')
        if numero < target:
            print('numero inserido é menor que o que estou pensando')
    print('parabéns! você acertou!')


jogo_de_adivinhacao()
