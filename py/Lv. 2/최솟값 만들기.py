def solution(A,B):
    A.sort()
    B = sorted(B,reverse=True)
    return sum(A[i] * B[i] for i in range(len(A)))


print("답: ",solution([1, 4, 2],	[5, 4, 4])) 
#29
print("답: ",solution([1,2],	[3,4]	))
#10