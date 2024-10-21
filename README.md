# 10월 21일
---

### 체스판 다시 칠하기
```
from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

board = list(input() for _ in range(M))
result = 64

for i in range(0, M-7):
    for j in range(0, N-7):

        cnt = 0
        for y in range(i, i+8) :
            for x in range(j, j+8) :
                if (y+x)%2 == 1 :
                    if board[y][x] == 'B' :
                        cnt += 1
                else :
                    if board[y][x] == 'W' :
                        cnt += 1
        result = min(cnt, 64-cnt, result)

print(result)
```

### N과 M 시리즈

- 2
```
import sys
input = sys.stdin.readline


def dfs(str, cnt):
    global path
    if cnt == M :
        print(*path)
        return

    else :
        for i in range(str, N+1) :
            path.append(i)
            dfs(i+1, cnt+1)
            path.pop()

    return

N, M = map(int, input().split())
path = []
dfs(1, 0)
```

- 4
```
import sys
input = sys.stdin.readline


def dfs(str, cnt):
    global path
    if cnt == M :
        print(*path)
        return

    else :
        for i in range(str, N+1) :
            path.append(i)
            dfs(i, cnt+1)
            path.pop()

    return

N, M = map(int, input().split())
path = []
dfs(1, 0)
```


- 5
```
import sys
input = sys.stdin.readline


def dfs(cnt, number):
    global path
    if cnt == M :
        print(*path)
        return

    else :
        for i in range(len(number)) :
            path.append(number[i])
            dfs(cnt+1, number[:i] + number[i+1:])
            path.pop()

    return

N, M = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
path = []
dfs(0, number)
```


- 헌내기는 친구가 필요해
```
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
```