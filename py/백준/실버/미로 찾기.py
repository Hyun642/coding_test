import sys,collections
input = sys.stdin.readline
n,m = (map(int,(input().split())))
board = [ list(map(int,input().strip())) for _ in range(n)] 
        
# 방향 전환 dr, dc
dr=[-1,1,0,0]
dc=[0,0,1,-1]
# stack 정의 및 (r,c,count) 넣기
que = collections.deque([(0,0,1)])
# 미리 0,0은 0으로 만들기
board[0][0] = 0
# while stack이 유지될 때까지
while que:
    # 방향 정의 r,c, 카운트업
    r,c, co = que.popleft()
    # 만약에 r,c가 n,m이면 return count
    if r == n-1 and c == m-1:
        print(co)
    # 4방위로 0이 아니면서 범위를 벗어나지 않고 board[nr][nc]가 1인 곳
    for i in range(4):
        nr= r+dr[i]
        nc= c+dc[i]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc]:
            # 스택에 넣기
            que.append((nr,nc,co+1))            
            # [nr][nc] = 0으로 바꾸기
            board[nr][nc] = 0





