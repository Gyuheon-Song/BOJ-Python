import sys
import copy
input = sys.stdin.readline

t = int(input())

def Determinant(mat) :
    det = mat[0][0]*(mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1]) - mat[0][1]*(mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0]) + mat[0][2]*(mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0])
    return det

for _ in range(t) :
    aug_mat = [list(map(int, input(). split())) for _ in range(3)]
    detA = Determinant(aug_mat)
    
    matA1 = copy.deepcopy(aug_mat)
    for i in range(3) :
        matA1[i][0] = matA1[i][3]  
    detA1 = Determinant(matA1)

    matA2 = copy.deepcopy(aug_mat)
    for i in range(3) :
        matA2[i][1] = matA2[i][3]  
    detA2 = Determinant(matA2)    

    matA3 = copy.deepcopy(aug_mat)
    for i in range(3) :
        matA3[i][2] = matA3[i][3]  
    detA3 = Determinant(matA3)

    print(detA1, detA2, detA3, detA)
    if detA == 0 :
        print("No unique solution")
        print()
    else :
        ans = [detA1/detA, detA2/detA, detA3/detA]
        print("Unique solution:", end = " ")
        for num in ans :
            if num == 0 :
                num = 0
                print("{:.3f}". format(num), end = " ")
            else :
                print("{:.3f}". format(num), end = " ")
        print()
        print()
    

