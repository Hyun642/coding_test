def solution(n, lost, reserve):
    take = [1] * (n+2)
    for r in reserve:
        take[r] +=1 
    for l in lost:
        take[l] -=1

    for i in range(1, n+1):
        if take[i] ==0:
            if take[i-1] == 2:
                take[i-1] -=1
                take[i] +=1
            elif take[i+1] == 2:
                take[i+1] -=1
                take[i] +=1
    count = 0
    for i in range(1,n+1):
        if take[i] >= 1:
            count +=1
    return count
print("답: ",solution( 5,	[2, 4],	[1, 3, 5]	))