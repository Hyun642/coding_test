def solution(n, computers):
    answer = 0
    visited = [0] * n

    def bfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j]== 1 and  not visited[j]:
                
                bfs(j)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer+=1


    return answer

print("답: ",solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))