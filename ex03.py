def tempconversor():
    print('Conversor de temperatura!\n')
    c = float(input('insira a temperatura em Celsius\n'))
    # F = C ∗ 1.8 + 32
    f = c * 1.8 + 32
    print(f'A temperatura em Fahrenheit é {f:.2f}')


tempconversor()
