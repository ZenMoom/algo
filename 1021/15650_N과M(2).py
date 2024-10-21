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
