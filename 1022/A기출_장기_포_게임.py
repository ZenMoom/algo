'''
전체 입력
set 변수 선언 (포 잡은 곳 중복 X)
for i, for j 로 2 찾기
    [i][j] == 2 : 함수 호출
------------------
dfs
움직임 3 번 다 썼으면 return
1. 방향 배열
    상 하 좌 우 for 문
        1부터 판 크기까지 for 문 => 포를 찾는데, 직선으로 2개가 있어야 함
            범위 확인 후 return
            2. 카운트
                1 을 만나면 1 증가
                1일 때 0 만남 -> 다시 dfs 소환 + i, j 와 위치 바꾸기(내가 있던 위치랑 바꾸는 거니까 0 <-> 2 해주기!)
                2일 때 1 만남 -> set 에 넣기 -> dfs 소환 + 거기로 갈 거면 위랑 똑같이 위치 바꾸기(근데 얜 0이 아니라 1이니까 0으로 바꾸고 교환, 이후 다시 1로 해줘야 함)
+ 움직이는 건 cnt 가 확인, 제어 => 먹을 수 있는지 없는지 조건은 eat_po 로 하되, 움직일 경우 0으로 reset 이 필요! 
------------------         
set 길이 출력

나머지는 구현하다 막히면 그때 생각해야지...
'''

def dfs(i, j, cnt) : # 좌표
    if cnt >= 3 :
        return
    for di, dj in DIR : 
        eat_po = 0
        for k in range(1, N) : 
            ni, nj = i+di*k, j+dj*k
            if 0 <= ni < N and 0 <= nj < N :
                if board[ni][nj] == 1 : eat_po += 1

                if eat_po == 1 and board[ni][nj] == 0 :
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                    dfs(ni, nj, cnt+1)
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]

                if eat_po == 2 and board[ni][nj] == 1 :
                    po_set.add((ni, nj))
                    board[ni][nj] = 0
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                    dfs(ni, nj, cnt+1)
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                    board[ni][nj] = 1
            

T = int(input())

for tc in range(1, T+1) : 
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    po_set = set()
    
    DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
    eat_po = 0

    for i in range(N) : 
        for j in range(N) : 
            if board[i][j] == 2 : 
                dfs(i, j, 0)
                break

    print(f'#{tc} {len(po_set)}')