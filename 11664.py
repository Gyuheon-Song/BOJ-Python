ax,ay,az,bx,by,bz,cx,cy,cz = map(int,input().split())

ans = 1e9

while True:
    mx,my,mz = (ax+bx)/2,(ay+by)/2,(az+bz)/2
    l = ((ax-cx)**2+(ay-cy)**2+(az-cz)**2)**0.5    # AC거리
    k = ((mx-cx)**2+(my-cy)**2+(mz-cz)**2)**0.5    # MC거리
    r = ((bx-cx)**2+(by-cy)**2+(bz-cz)**2)**0.5    # BC거리

    if abs(ans-k) <= 1e-6:  # 정답과 오차가 충분히 적은 경우 루프탈출
        print('%0.10f'%ans)
        exit()
    if k < ans:  # MC거리가 기존의 정답보다 작은 경우 정답 갱신
        ans = k
    if l > r:    # 만약 왼쪽점과 C점과의 거리가 오른쪽 점과 C점과의 거리보다 멀다면 중점을 왼쪽점으로 갱신하여 범위를 줄인다
        ax,ay,az = mx,my,mz
    else:
        bx,by,bz = mx,my,mz