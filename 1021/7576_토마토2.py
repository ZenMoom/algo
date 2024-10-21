from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split()) # M 가로 N 세로 H 높이

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

tomato = deque()

for h in range(H) :
    for n in range(N) :
        for m in range(M) :
            if arr[h][n][m] == 1 :
                tomato.append((h, n, m))

D = [(0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]

while tomato :
    h, i, j = tomato.popleft()

    for dh, di, dj in D :
        nh, ni, nj = h+dh, i + di, j+dj
        if 0<=nh<H and 0<= ni< N and 0<= nj < M and arr[nh][ni][nj] == 0 :
            arr[nh][ni][nj] = arr[h][i][j] + 1
            tomato.append((nh, ni, nj))


Day = 0
for a in arr :
    for n in a:
        for toma in n :
            if toma == 0 :
                print(-1)
                exit(0)
            else :
                Day = max(Day, toma)

print(Day-1)