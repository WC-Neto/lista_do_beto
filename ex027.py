def p_frequente():
    from collections import Counter
    texto = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. '''

    palavras = texto.lower().split()

    contador = Counter(palavras)

    mais_comuns = contador.most_common(5)

    print("As 5 palavras mais frequentes no texto são:")
    for palavra, frequencia in mais_comuns:
        print(f"{palavra}: {frequencia} vezes")


p_frequente()
