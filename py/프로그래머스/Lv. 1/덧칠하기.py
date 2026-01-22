def solution(n, m, section):
    last_painted = 0
    painting_count = 0
    for x in section:
        if x > last_painted :
            last_painted = x+m-1
            painting_count +=1 
    
    return painting_count

print("답: ",solution(8,	4,	[2, 3, 6]))
print("답: ",solution(5,	4,	[1, 3]	))
print("답: ",solution(4,	1,	[1, 2, 3, 4]))