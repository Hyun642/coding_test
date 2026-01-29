def solution(a,	b,	n):
    sum = 0
    while n >= a:
        div,mod = divmod(n,a)
        sum = sum + (div*b)
        n= div*b  + mod
    return sum

print("답: ",solution(3,	1,	20	))