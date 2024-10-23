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


# 10월 22일
- 장기 포 게임 로직만 짜고 구현 실패 (컨디션 난조)
---

# 10월 23일

### 장기 포 게임
```
def dfs(i, j, cnt) : # 좌표, 좌표, 움직인 횟수
    if cnt >= 3 :
        return
    for di, dj in DIR : # 방향 배열
        eat_po = 0 # 그 자리에서 0부터 시작
        for k in range(1, N) : # 직선으로 움직여야 하는 조건
            ni, nj = i+di*k, j+dj*k 
            if 0 <= ni < N and 0 <= nj < N :
                if board[ni][nj] == 1 : eat_po += 1 # eat_op == 2 + ninj == 1 이면 먹을 수 있는 포의 조건 충족

                if eat_po == 1 and board[ni][nj] == 0 : # 뛰어넘을 수 있는 조건으로, 이동함
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                    dfs(ni, nj, cnt+1)
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]

                if eat_po == 2 and board[ni][nj] == 1 : # 똑같이 뛰어넘을 수 있는 조건 + 먹을 수 있는 조건으로 먹고 이동
                    po_set.add((ni, nj))
                    board[ni][nj] = 0 # 근데 얘는 위랑 다르게 0 <-> 2 가 아니라 1 <-> 2이므로 똑같은 곳 돌아올 수 있으므로 0으로 바꿔치기 후 이동
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                    dfs(ni, nj, cnt+1)
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                    board[ni][nj] = 1
            

T = int(input())

for tc in range(1, T+1) : 
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    po_set = set() # 똑같은 위치의 포는 카운트하면 안 됨 
    
    DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
    eat_po = 0

    for i in range(N) : 
        for j in range(N) : 
            if board[i][j] == 2 : 
                dfs(i, j, 0)
                break

    print(f'#{tc} {len(po_set)}')
``` 