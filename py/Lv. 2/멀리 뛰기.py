def solution(n):
    x,y = 0,1
    for _ in range(n-1):
        x,y = y, x+y 
    
    return( x+y)%1234567

print("답: ",solution(4))
# 5
# print("답: ",solution(3))
# 3