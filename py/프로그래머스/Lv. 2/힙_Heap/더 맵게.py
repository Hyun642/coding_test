import heapq
def solution(scoville,	K):
    ans =0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + (second*2)
        heapq.heappush(scoville,new)
        ans+=1
    return ans if scoville[0] >= K else -1
        
print("답: ",solution([1, 2, 3, 9, 10, 12],	7))
print("답: ",solution([1,1],	5))
print("답: ",solution([10,12],	5))