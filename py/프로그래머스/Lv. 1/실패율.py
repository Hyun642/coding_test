def solution(n, stages):
    answer = {}
    total_players = len(stages)

    for stage in range(1,n+1):
        if total_players > 0:
            count = stages.count(stage)
            answer[stage] = count/total_players
            total_players -= count
        else:
            answer[stage] = 0

    return sorted(answer, key=lambda x:-answer[x])



print("답: ",solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]	))
print("답: ",solution(4,	[4,4,4,4,4]))