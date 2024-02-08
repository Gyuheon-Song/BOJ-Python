import sys
input = sys.stdin.readline
result = 0

def Merge_sort(s, e) :
    global result
    if e-s < 1 :   # 토막 사이즈가 더이상 자를 수 없을 때 리턴
        return
    m = int(s + (e - s) / 2)      # 비교할 토막 사이즈
    Merge_sort(s, m)   # 재귀로 병합정렬 구현
    Merge_sort(m+1, e)
    
    for i in range(s, e+1) :
        tmp[i] = lst[i]

    k = s   # 정렬을 시행하는 과정에서 데이터를 순차적으로 넣을 인덱스변수
    index1 = s
    index2 = m+1
    while index1 <= m and index2 <= e :
        if tmp[index1] > tmp[index2] :     
            lst[k] = tmp[index2]
            result += (index2 - k)     # 앞으로 이동한 칸 만큼 swap이 일어난다
            k += 1
            index2 += 1
        else :
            lst[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m :     # 위의 포인터이동을 하며 정렬을 시행했음에도
        lst[k] = tmp[index1]       # 포인터가 더이상 이동할 수 없는 정렬상태일 때 
        k += 1
        index1 += 1
    while index2 <= e :
        lst[k] = tmp[index2]
        k += 1
        index2 += 1

n = int(input())
lst = [0] + list(map(int, input(). split()))
tmp = [0] * (n+1)
Merge_sort(1, n)
print(result)
