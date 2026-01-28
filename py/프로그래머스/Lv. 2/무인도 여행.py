import collections
def solution(maps):
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    visited=[[False]* len(maps[0]) for _ in range(len(maps))]
    
    ans=[]

    for r,_ in enumerate(maps):
        for c,_ in enumerate(maps[r]):
            if maps[r][c] !='X' and not visited[r][c]:
                que = collections.deque([(r,c)])
                food=0
                visited[r][c] = True
                while que:
                    cur_i, cur_j = que.popleft()
                    food+= int(maps[cur_i][cur_j])
                    for k in range(4):
                        nr = cur_i + dr[k]
                        nc = cur_j + dc[k]
                        if 0 <= nr < len(maps) and  0 <= nc < len(maps[0]):
                            if not visited[nr][nc] and maps[nr][nc] !='X':
                                visited[nr][nc]=True
                                que.append((nr,nc))
                ans.append(food)
    return sorted(ans) if ans else [-1]

print("답: ",solution(["X591X","X1X5X","X231X", "1XXX1"]	))