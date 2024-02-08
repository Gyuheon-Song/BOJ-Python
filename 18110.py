import sys
input = sys.stdin.readline

def round(num) :
    return int(num) + [0, 1][num - int(num) >= 0.5]  #int(num) -> 정수부!!

n = int(input())
if n == 0 : print(0)
else :
    nums = sorted([int(input()) for _ in range(n)])
    excpt = round(n * 0.15)
    if excpt > 0 : 
        nums = nums[excpt : -excpt]
    print(round(sum(nums) / (n - excpt*2)))


