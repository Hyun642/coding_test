import math
def solution(n, m):
    # return [math.gcd(n,m), math.lcm(n,m)]
    a,b = n,m
    while b > 0 :
        a,b = b, a%b
    gcd= a

    lcm = n * m // gcd    

    return [gcd, lcm]




print("답: ",solution(3,	12)) 
#[3, 12]
print("답: ",solution(2,	5	)) 
#[1, 10]