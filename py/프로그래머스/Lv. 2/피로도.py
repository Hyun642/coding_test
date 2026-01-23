import itertools
def solution(k, dungeons):
    permutations= itertools.permutations(dungeons)
    max_go = 0
    for per in permutations:
        now= k
        go = 0
        for a,b in per:
            if now >= a:
                now -= b
                go +=1
            else:
                break
        if go > max_go:
                    max_go = go
    return max_go


print("답: ",solution(80,	[[80,20],[50,40],[30,10]]))
# print("답: ",solution())