import math
x1, y1, z1, x2, y2, z2 = map(int, input(). split())
n = int(input())
stick = list(map(int, input(). split()))
stick.sort()

dx = abs(x2 - x1)
dy = abs(y2 - y1)
dz = abs(z2 - z1)

# 두 점 사이의 3차원 거리
dist = math.sqrt(pow(dx, 2) + pow(dy, 2) + pow(dz, 2))

if sum(stick) < dist :   # 막대기들을 가장 길게 연결해도 두 점 사이의 거리보다 짧은 경우 연결 불가
    print("NO")
else :  # 막대기들의 길이의 합이 두 점 사이의 거리보다 긴 경우
    longest = stick[-1]   # 가장 긴 막대기 제외
    stick.pop()
    if longest - sum(stick) > dist :    # 시작점에서 가장 긴 막대기로 시작했을 때 그 막대기의 끝에서
                                        # 두번째 점까지 연결이 안되는 경우 => 가장 긴 막대기를 제외하고
                                        # 나머지 막대기들을 다 이어도 두번째 점으로 돌아오지 못하는 경우
        print("NO")
    else:
        print("YES")

        

