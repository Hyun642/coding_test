import collections
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

que = collections.deque([])
count = 0
p_size = [0]
#포문 - while문으로 방문한 곳이 아니라면 방문하고 0으로 만들기
for x in range(len(board)):
    for y in range(len(board[x])):
        if board[x][y]:
            count += 1
            que.append((x,y))
            board[x][y] = 0
            size=0
            while que:
                r,c =que.popleft()
                size+=1
                for i in range(4):
                    nr = r+dr[i]
                    nc = c+dc[i]
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc]:
                        que.append((nr,nc))
                        board[nr][nc] = 0
            p_size.append(size)

print(count)
print(max(p_size))