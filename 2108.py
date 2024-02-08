import sys
input=sys.stdin.readline

n = int(input())
arr = []

for i in range(n) :
    arr.append(int(input()))

arr.sort()
print(round(sum(arr)/len(arr))) # average 
print(arr[n//2]) # mid point

dic = {} # 반복된 수를 딕셔너리에 넣는다
for i in arr :
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1

mode_repeat_num = max(dic.values()) #가장 많이 반복된 수의 반복횟수
max_mode = []

for i in dic :             #가장 많이 반복된 수를 리스트화
    if mode_repeat_num == dic[i] :
        max_mode.append(i)

if len(max_mode) > 1 :      #리스트에 최빈값 여러개 있을때
    print(max_mode[1])      #두번쨰 큰 값

else :
    print(max_mode[0])      #최빈값 하나일때 그대로

print(max(arr)-min(arr))    #범위
