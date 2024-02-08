n = int(input())
num_lst = list(map(int, input(). split()))
m = int(input())
chk_lst = list(map(int, input(). split()))

def solution(num_lst, chk_lst) :
    num_lst.sort()  
    answer = []
    for num in chk_lst :
        left = 0
        right = len(num_lst) - 1
        while left <= right :
            mid = (left + right) // 2
            if num > num_lst[mid] :
                left = mid + 1
            elif num == num_lst[mid] :
                answer.append(1)
                break
            else :
                right = mid - 1        
        if left > right :
            answer.append(0)
        
    return answer

for item in solution(num_lst, chk_lst) :
    print(item)


# n = int(input())
# nums = set(map(int, input(). split()))
# m = int(input())
# chk = list(map(int, input(). split()))

# for num in chk :
#     if num in nums :
#         print(1)
#     else :
#         print(0)




    
        





        



    


            