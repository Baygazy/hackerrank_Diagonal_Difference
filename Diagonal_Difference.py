    # def start
    alls = 0
    alls2 = 0

    for x in range(n):
        alls += arr[x][x]
        print(alls)
    s = -1
    for i in range(n):
        alls2 += arr[i][i+s]     # каждый раз i увеличивается на 1 вправо, поэтому
        s += (-2)                # мы уменьшаем его на 2 влево каждый раз
        print(alls2)
    otvet = abs(alls - alls2)

    return otvet

    # def stop