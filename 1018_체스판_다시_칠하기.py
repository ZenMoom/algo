'''
BFS, DFS 사용하려 했는데, 실행 시간에서 터졌고 완전탐색으로 풀이
다른 방식이 있나 찾아봤는데, 문제 알고리즘 분류부터 브루트포스 알고리즘이라 완탐으로 끝.
'''
'''
def WorB(i, j, c) :
    global result
    q = deque()
    q.append((i, j, c))
    cnt = 0
    visited = list([False] * N for _ in range(M))

    while q:
        y, x, idx = q.popleft()
        if board[y][x] != color[idx] and visited[y-i][x-j] == False:
            cnt += 1
            visited[y - i][x - j] = True

        if cnt >= result: break

        for ni, nj in D:
            ny = y + ni
            nx = x + nj
            if 0 <= ny < i + 8 and 0 <= nx < j + 8:
                q.append((ny, nx, (idx+1)%2))

    if cnt < result:
        result = cnt
    return
'''

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