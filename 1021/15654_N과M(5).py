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