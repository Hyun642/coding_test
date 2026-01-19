from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dr= [1,0,-1,0]
    dc= [0,1,0,-1]
    queue =deque([[0,0,1]])
    maps[0][0] = 0
    while queue:
        r,c,dist = queue.popleft()

        if r== n-1 and c==m-1:
            return dist

        for i in range(4):
            nr = r +dr[i]
            nc = c +dc[i]
            if 0<=nr<n and 0<=nc<m and maps[nr][nc] ==1:
                queue.append([nr,nc,dist+1])
                maps[nr][nc] = 0
    
    return -1

print("답: ",solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))