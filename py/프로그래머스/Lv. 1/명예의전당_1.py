import heapq
def solution(k,	score):
    
    answer = []
    loot=[]
    for i in score:
        heapq.heappush(loot,i)
       
        if len(loot) > k:
                heapq.heappop(loot)
        answer.append(loot[0])

        print(loot)
    return answer



print("답: ",solution(3,	[10, 100, 20, 150, 1, 100, 200]))