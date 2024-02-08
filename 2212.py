n = int(input())
k = int(input())

if n <= k :
    print(0)

else:
    sensor = list(map(int, input(). split()))
    sensor.sort()
    mn = sensor[0]
    mx = sensor[-1]
    diff = []
    for i in range(len(sensor)-1) :
        diff.append(sensor[i+1]-sensor[i])

    diff.sort(reverse = True)

    ans = 0
    for j in range(k-1) :
        ans += diff[j]

    print(mx-mn-ans)

