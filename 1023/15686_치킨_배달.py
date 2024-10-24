import sys
input = sys.stdin.readline

def find_ck(live_cks):
    global result

    tmp = 0
    for H in home :
        temp = []
        for cks in live_cks :
            temp.append(abs(cks[0]-H[0]) + abs(cks[1]-H[1]))
        tmp += min(temp)
        if tmp >= result : return
    if tmp < result : 
        result = tmp
    

def temp(cnt, i) : 
    global live_cks

    if cnt == M : 
        # 함수 호출
        find_ck(live_cks[:])
        return
    
    else :
        for y in range(i, len(town_ck)) :
            live_cks.append(town_ck[y])
            temp(cnt+1, y+1)
            live_cks.pop()


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]

home = []
town_ck = []
live_cks = []
result = float('inf')

for i in range(N) : 
    for j in range(N) :
        if town[i][j] == 1 : home.append((i, j))
        elif town[i][j] == 2 : town_ck.append((i, j))

temp(0, 0) 
print(result)