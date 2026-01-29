from collections import deque

def solution(numbers, target):
    queue = deque([0])
    
    for num in numbers:
        next_step=[]
        while queue:
            current_sum = queue.popleft()
            next_step.append(current_sum+num)
            next_step.append(current_sum-num)
        queue = deque(next_step)

    return queue.count(target)

print("답: ",solution([1, 1, 1, 1, 1],	3))
##5
print("답: ",solution([4, 1, 2, 1],4))