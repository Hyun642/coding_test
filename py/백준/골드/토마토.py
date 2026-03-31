import sys, collections

def s():
    input = sys.stdin.readline
    m,n = (map(int,input().split()))
    board = [list(map(int,input().strip().split())) for _ in range(n)] 
    unripe_tmt= 0

    dr=[1,-1,0,0]
    dc=[0,0,1,-1]

    #que 정의
    que = collections.deque()
    #for문 que에 1 위치 저장
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                que.append((i,j,0))
            elif board[i][j] == 0:
                unripe_tmt+=1
                
    day=0
    # while que
    while que:
        # r,c,day
        r,c,addday = que.popleft()
        day=addday
        # for문 4방위
        # co=0
        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] ==0:
                    que.append((nr,nc,day+1))
                    unripe_tmt-=1

                    board[nr][nc]= 1 
                    # co+=1
        # 주변에 0이 없으면 return
        # if not co:
        #     return day
    return day if not unripe_tmt else -1
print(s())