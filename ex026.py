def mesclad():
    dicionario1 = {'nome': 'ana', 'dinheiro': '23'}
    dicionario2 = {'nome': 'luan', 'dinheiro': '25'}
    dicionario3 = {}

    for chave in set(dicionario1.keys()).union(dicionario2.keys()):
        if chave == 'dinheiro':
            dicionario3[chave] = int(
                dicionario1[chave]) + int(dicionario2[chave])
        if chave == 'nome':
            dicionario3[chave] = f"{dicionario1[chave]} e {dicionario2[chave]}"

    print(dicionario3)


mesclad()
