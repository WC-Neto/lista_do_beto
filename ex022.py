def vogais_e_consoantes():
    frase = str(input('insira uma frase\n'))
    frase.lower()
    vogais = []
    consoantes = []
    for c in frase:
        if c in 'aeiou':
            vogais.append(c)
        if c in 'bcdfghjklmnpqrstvwxyz':
            consoantes.append(c)
    print(f'o numero de vogais é {len(vogais)}')
    print(f'o numero de consoantes é {len(consoantes)}')


vogais_e_consoantes()
