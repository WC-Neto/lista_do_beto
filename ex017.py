def ordenando():
    print('ordenando a lista entre positivos e negativos')
    general_list = [3, -1, 1, -3, 9, -7]
    newlist = []
    i = 0
    for i in range(0, 6):
        if general_list[i] < 0:
            newlist.append(general_list[i])
            i += 1
    for i in range(0, 6):
        if general_list[i] > 0:
            newlist.append(general_list[i])
            i += 1
    print(newlist)


ordenando()
