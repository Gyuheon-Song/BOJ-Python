import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
arr = [list(map(int, input(). split())) for _ in range(n)]
white = 0
blue = 0

def solution(x, y, z) :
    global white, blue
    color = arr[x][y]
    for i in range(x, x+z) :
        for j in range(y, y+z) :
            if color != arr[i][j] :
                solution(x, y, z//2)
                solution(x+z//2, y, z//2)
                solution(x, y+z//2, z//2)
                solution(x+z//2, y+z//2, z//2)
                return
    if color == 0 :
        white += 1
    else :
        blue += 1

solution(0, 0, n)
print(white, blue, sep = "\n")

