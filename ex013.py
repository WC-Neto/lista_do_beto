def media_e_acima():
    print('media e acima da média')
    media = [7.0, 7.1, 2.3, 0, 2.4, 9.8, 10]
    i = 0
    acima = []
    for i in range(0, 7):
        if media[i] >= 7:
            acima.append(media[i])
    print(acima)


media_e_acima()
