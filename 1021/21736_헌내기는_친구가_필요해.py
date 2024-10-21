from collections import  deque
import sys
input = sys.stdin.readline



N, M = map(int, input().split())
arr = list(input() for _ in range(N))

cnt = 0
q = deque()
D = [(1,0), (0,1), (-1,0),(0,-1)]
visited = list([False]*M for _ in range(N))

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 'I' :
            q.append((i, j))
            visited[i][j] = True
            break

while q :
    i, j = q.popleft()
    if arr[i][j] == 'P' : cnt += 1
    for di, dj in D :
        ni = i + di
        nj = j + dj
        if (0<=ni<N and 0<= nj < M and arr[ni][nj] != 'X'
                and visited[ni][nj] == False):
            q.append((ni, nj))
            visited[ni][nj] = True

if cnt == 0 :
    print('TT')
else : print(cnt)