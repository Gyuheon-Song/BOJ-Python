n, m = map(int, input(). split())
nums = list(map(int, input(). split()))

current = sum(nums[0:m])
left = 0
right = m
summation = current
while right <= len(nums) - 1 :
    current = current + nums[right] - nums[left]
    summation = max(summation, current)
    left += 1
    right += 1

print(summation)


    

