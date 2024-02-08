import sys
input = sys.stdin.readline
n, m = map(int, input(). split())
board = []
for i in range(n) :
    board.append(list(input().strip()))
ans_w = 32
ans_b = 32

for i in range(n-7) : 
    for j in range(m-7) :
        w_start = 0
        b_start = 0
        for a in range(i, i+8) :
            for b in range(j, j+8) :
                if (a + b) % 2 == 0 :
                    if board[a][b] != "W" :
                        w_start += 1
                    elif board[a][b] != "B" :
                        b_start += 1
                else :
                    if board[a][b] != "W" :
                        b_start += 1
                    elif board[a][b] != "B" :
                        w_start += 1
        ans_w = min(w_start, ans_w)
        ans_b = min(b_start, ans_b)

print(min(ans_w, ans_b))