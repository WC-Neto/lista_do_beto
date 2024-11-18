def fibonacci():
    print('fibonacci')
    n = int(input('quantos números da sequencia desejam ver?'))
    contador = 0
    n0 = 0
    n1 = 1
    n2 = 0
    while contador < n:
        n0 = n1
        n1 = n2
        n2 = n0 + n1
        contador += 1
        print(n2, end=' ')


fibonacci()
