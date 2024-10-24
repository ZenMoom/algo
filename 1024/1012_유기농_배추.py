from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j) :
    if arr[i][j] == 0 or visited[i][j] == True:
        return False
    if arr[i][j] == 1:
        q.append((i, j))
        while q :
            i, j = q.popleft()
            visited[i][j] = True
            for di, dj in D :
                ni = i +di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == False: 
                    q.append((ni, nj))
                    arr[ni][nj] = 0
        return True


T = int(input()) 

for tc in range(T) : 
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)] # N : 세로 M : 가로
    for k in range(K) :
        j, i = map(int, input().split())
        arr[i][j] = 1
    cnt = 0
    q = deque()
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * M for _ in range(N)]

    for i in range(N) : 
        for j in range(M) :
            if bfs(i, j) : cnt += 1 
    
    print(cnt)                        