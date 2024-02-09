import math
n, m = map(int, input(). split())

def threeEdges(x1, y1, x2, y2, x3, y3) :   # 주어진 세 점으로 이루어진 삼각형의 세 변의 길이를 오름차순 정렬된 리스트로 반환
    e1 = math.sqrt(pow(abs(x2-x1), 2) + pow(abs(y2-y1), 2))
    e2 = math.sqrt(pow(abs(x3-x2), 2) + pow(abs(y3-y2), 2))
    e3 = math.sqrt(pow(abs(x3-x1), 2) + pow(abs(y3-y1), 2))
    lst = [e1, e2, e3]
    lst.sort()
    return lst

def Inclination(x1, y1, x2, y2) :    # 두 점 사이의 기울기를 반환
    if y2 == y1 :    # 두 점이 같은 열에 있는 경우 문제에서 나올 수 있는 최대 기울기인 10 보다 큰 수 반환하도록 설정
        return 12
    return (x2-x1)/(y2-y1)   # 다른 열에 있는 경우 기울기 반환

visited = [[False]*(n+1) for _ in range(m+1)]   # 세 점의 순열을 만들기 위한 방문배열
edges = []
points = []

def threePoints(r, c) :    # 삼각형을 만들 수 있는 조건에 있는 세 점을 반환
    global visited, points
    if len(points) == 3 :    # 점 세개가 선택된 경우
        # 만약 세 점이 한 행이나 열 상에 존재한다면
        if points[0][0] == points[1][0] == points[2][0] or points[0][1] == points[1][1] == points[2][1] :
            return  # 다음 순열 선택
        # 만야 세 점이 한 대각선에 존재한다면
        elif Inclination(points[0][0], points[0][1], points[1][0], points[1][1]) == Inclination(points[1][0], points[1][1], points[2][0], points[2][1]) :
            return   # 다음 순열 선택
        edges.append(threeEdges(points[0][0],points[0][1],points[1][0],points[1][1], points[2][0], points[2][1]))
        return
    for i in range(r+1) :
        for j in range(c+1) :
            if not visited[i][j] :   # 아직 선택하지 않은 점이라면
                visited[i][j] = True   # 방문표시를 하고
                points.append([i, j])   # 점을 순열에 포함시킨다
                threePoints(r, c)    # 재귀
                visited[i][j] = False
                points.pop()

threePoints(m, n)
# 세 변의 길이의 조합이 다 다른 경우 모두가 다른 삼각형이므로
# 세 변의 길이의 조합을 중복없이 저장
edges = list(set(tuple(sublst) for sublst in edges))
print(len(edges))   # 세 변의 길이가 모두 다른 변의 조합의 수가 곧 다른 삼각형들의 개수

            



