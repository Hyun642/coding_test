import math, functools
def solution(arr):
    return  functools.reduce(lambda x,y:(x*y)//math.gcd(x,y), arr)




print("답: ",solution([2,6,8,14]))
# 168
# print("답: ",solution([1,2,3]))
# 6