def solution(n):
    a,b=0,1
    for i in range(2,n+1):
        if i == n:
            return (a+b)%1234567
        a,b = b,a+b



print("답: ",solution(3	)) 
#	2
print("답: ",solution(5)) 
#   5