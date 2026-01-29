def solution(n):
    grid = [[0]*n for i in range(n)] 
    dr=[1,0,-1]
    dc=[0,1,-1]
    r,c = 0,0
    direction = 0
    max_num = n * (n + 1) // 2  
    for i in range(1,max_num+1):
        grid[r][c] = i

        if i == max_num:
            break

        nr=r+dr[direction%3]
        nc=c+dc[direction%3]

        if nr < 0 or nr >= n or nc < 0 or nc > nr or grid[nr][nc] != 0:
            direction += 1
            nr = r + dr[direction % 3]
            nc = c + dc[direction % 3]
        r, c = nr, nc

    answer = []
    for row in grid:
        for val in row:
            if val != 0:
                answer.append(val)
                
    return answer


print("답: ",solution(4	))