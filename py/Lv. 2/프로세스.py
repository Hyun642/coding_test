import collections
def solution(priorities, location):
    answer = 0
    queue = collections.deque([(p,i) for i,p in enumerate(priorities)])
    while queue:
        current = queue.popleft()
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            answer+=1
            if current[1] == location:
                return answer


print("답: ",solution([1, 1, 9, 1, 1, 1],0))