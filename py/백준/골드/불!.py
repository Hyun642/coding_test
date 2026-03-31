import sys
from collections import deque
def s():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]

    fire_b = [[-1] * C for i in range(R)]
    person_b = [[-1] * C for i in range(R)]

    fire_que = deque()
    person_que = deque()

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'F':
                fire_b[i][j] = 0
                fire_que.append((i,j))
            if board[i][j] == 'J':
                person_b[i][j] = 0
                person_que.append((i,j))

    dr = [1,-1,0,0]
    dc = [0,0,-1,1]

    while fire_que:
        r,c = fire_que.popleft()
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != '#' and fire_b[nr][nc] == -1:
                fire_b[nr][nc] = fire_b[r][c] + 1
                fire_que.append((nr,nc))
    while person_que:
        r,c = person_que.popleft()
        
        if r <= 0 or r >= R-1 or c <= 0 or c >= C-1:
            return person_b[r][c]+1

        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if fire_b[nr][nc] > person_b[r][c] + 1 or fire_b[nr][nc] == -1 :
                if person_b[nr][nc] == -1 and board[nr][nc] != '#' :
                    person_b[nr][nc] = person_b[r][c] + 1
                    person_que.append((nr,nc))
    return 'IMPOSSIBLE'
    
print(s())