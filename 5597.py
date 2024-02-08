attendance = []

for i in range(30) :
    attendance.append(i+1)

for j in range(28) :
    std_num = int(input())
    attendance.remove(std_num)

for item in attendance :
    print(item)
    

    

