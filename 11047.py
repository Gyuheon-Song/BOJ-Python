n, k = map(int, input(). split())
nums = []

for i in range(n) :
    nums.append(int(input()))

def solution(nums, k) :
    cnt = 0
    nums.sort(reverse = True)
    for i in nums :
        if i > k :
            continue
        else :
            cnt += k//i
            k -= (k//i)*i
            
    return print(cnt)

solution(nums, k)




