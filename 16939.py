import copy
from collections import deque
cube = list(map(int, input(). split()))

def SolvedCube(t) :
    for i in range(0, 21, 4) :
        if len(set(t[i:i+4])) == 1 :
            continue
        else :
            return False
    return True

def RotateCube(k) :    # 큐브의 가로, 세로, 높이를 위아래로 회전시켜 보기  => 총 6회 한쪽 면만 돌려보면 된다
    # 오른쪽 면 아래로 돌려보기
    initcube = copy.deepcopy(k)
    tmp1, tmp2 = initcube[1], initcube[3]
    initcube[1], initcube[3] = initcube[22], initcube[20]
    tmp3, tmp4 = initcube[5], initcube[7]
    initcube[5], initcube[7] = tmp1, tmp2 
    tmp1, tmp2 = initcube[9], initcube[11]
    initcube[9], initcube[11] = tmp3, tmp4
    initcube[20], initcube[22] = tmp2, tmp1
    if SolvedCube(initcube) :
        print(1)
        return
    
    # 오른쪽 면 위로 돌려보기
    initcube = copy.deepcopy(k)
    tmp1, tmp2 = initcube[1], initcube[3]
    initcube[1], initcube[3] = initcube[5], initcube[7]
    tmp3, tmp4 = initcube[20], initcube[22]
    initcube[20], initcube[22] = tmp2, tmp1 
    tmp1, tmp2 = initcube[9], initcube[11]
    initcube[9], initcube[11] = tmp4, tmp3
    initcube[5], initcube[7] = tmp1, tmp2
    if SolvedCube(initcube) :
        print(1)
        return
    
    # 윗면 왼쪽으로 돌려보기
    initcube = copy.deepcopy(k)
    tmp1, tmp2 = initcube[0], initcube[1]
    initcube[0], initcube[1] = initcube[12], initcube[14]
    tmp3, tmp4 = initcube[17], initcube[19]
    initcube[17], initcube[19] = tmp1, tmp2 
    tmp1, tmp2 = initcube[10], initcube[11]
    initcube[10], initcube[11] = tmp4, tmp3
    initcube[12], initcube[14] = tmp1, tmp2
    if SolvedCube(initcube) :
        print(1)
        return

    # 윗면 오른쪽으로 돌려보기
    initcube = copy.deepcopy(k)
    tmp1, tmp2 = initcube[0], initcube[1]
    initcube[0], initcube[1] = initcube[17], initcube[19]
    tmp3, tmp4 = initcube[12], initcube[14]
    initcube[12], initcube[14] = tmp2, tmp1 
    tmp1, tmp2 = initcube[10], initcube[11]
    initcube[10], initcube[11] = tmp3, tmp4
    initcube[17], initcube[19] = tmp2, tmp1
    if SolvedCube(initcube) :
        print(1)
        return

    # 앞면 왼쪽으로 돌려보기
    initcube = copy.deepcopy(k)
    tmp1, tmp2 = initcube[6], initcube[7]
    initcube[6], initcube[7] = initcube[14], initcube[15]
    tmp3, tmp4 = initcube[18], initcube[19]
    initcube[18], initcube[19] = tmp1, tmp2 
    tmp1, tmp2 = initcube[22], initcube[23]
    initcube[22], initcube[23] = tmp3, tmp4
    initcube[14], initcube[15] = tmp1, tmp2
    if SolvedCube(initcube) :
        print(1)
        return

    # 앞면 오른쪽으로 돌려보기
    initcube = copy.deepcopy(k)
    tmp1, tmp2 = initcube[6], initcube[7]
    initcube[6], initcube[7] = initcube[18], initcube[19]
    tmp3, tmp4 = initcube[14], initcube[15]
    initcube[14], initcube[15] = tmp1, tmp2 
    tmp1, tmp2 = initcube[22], initcube[23]
    initcube[22], initcube[23] = tmp3, tmp4
    initcube[18], initcube[19] = tmp1, tmp2
    if SolvedCube(initcube) :
        print(1)
        return
    print(0)
    return

RotateCube(cube)




    

        

        