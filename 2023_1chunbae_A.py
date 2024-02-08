
picture = [list(map(str, input(). split())) for _ in range(15)]

for i in range(15) :
    for j in range(15) :
        if picture[i][j] == 'w' :
            print("chunbae")
            exit()
        elif picture[i][j] == 'b' :
            print('nabi')
            exit()
        elif picture[i][j] == 'g' :
            print('yeongcheol')
            exit()
        else :
            continue