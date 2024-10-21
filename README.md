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