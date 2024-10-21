from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

tomato = deque()

for i in range(N) :
    for j in range(M) :
        if box[i][j] == 1 :
            tomato.append((i, j))

D = [(1,0), (0,1), (-1,0), (0, -1)]


def BFS(tomato):
    while tomato :
        i, j = tomato.popleft()
        for k in range(4) :
            ni = i+D[k][0]
            nj = j+D[k][1]
            if 0<=ni<N and 0<=nj<M and box[ni][nj] == 0 :
                tomato.append((ni, nj))
                box[ni][nj] = box[i][j] + 1
    return box

temp = BFS(tomato)

Day = 1
for n in temp :
    if 0 in n :
      Day = 0
      break
    else :
        Day = max(Day, max(n))

if Day == 1 :
    print(0)
elif Day == 0 :
    print(-1)
else :
    print(Day-1)
