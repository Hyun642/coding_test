import collections
def solution(queue1, queue2):

    sum1,sum2= sum(queue1),sum(queue2)
    queue1 = collections.deque(queue1)
    queue2 = collections.deque(queue2)
    if (sum1+sum2) % 2:
        return -1

    limit=(len(queue1)) * 3
    i=0

    while i<= limit:
        if sum1== sum2:
            return i
        elif sum1 > sum2:
            me = queue1.popleft()
            queue2.append(me)
            sum1 -= me
            sum2 += me
        else:
            me = queue2.popleft()
            queue1.append(me)
            sum2 -= me
            sum1 += me
        i+=1
    return -1
    

print("답: ",solution([3, 2, 7, 2],	[4, 6, 5, 1]	))
print("답: ",solution([1, 1], [1, 5]	))