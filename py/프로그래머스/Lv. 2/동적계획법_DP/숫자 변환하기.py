import collections
def solution(x,	y,	n):
    if x==y:
        return 0
    que = collections.deque([(x,0)])
    
    s = {x}
    while que:
        c_sum, count = que.popleft()
        for i in [c_sum+n,c_sum*2,c_sum*3]:
            if i==y:
                return count+1
            elif i <= y and i not in s:
                s.add(i)
                que.append((i,count+1))
    return -1