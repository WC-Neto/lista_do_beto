def contador_de_palavras():
    print('Apenas palavras unicas')
    frase = str(input('insira um frase\n')).split()
    palavras_unicas = set(frase)
    contador = len(palavras_unicas)
    print(f'Na frase digitada, as palavras {
          palavras_unicas} são unicas totalizando {contador}')


contador_de_palavras()
