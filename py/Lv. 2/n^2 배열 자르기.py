def solution(n, left, right):
    answer = []
    
    for k in range(left,right+1):
        r= k//n
        c= k%n
        answer.append(max(r,c)+1)

    return answer

print("답: ",solution(3,	2,	5))