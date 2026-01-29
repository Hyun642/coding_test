def solution(n):
    a=0
    b=1
    for _ in (range(1,n)):
        a,b = b,(a+b)%1000000007
    return (a+b)




print("답: ",solution(3))