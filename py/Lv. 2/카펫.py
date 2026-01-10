def solution(brown, yellow):
    sum = brown + yellow

    for h in range(3,int(sum**0.5)+1):
        if sum % h == 0:
            w= sum // h

            if (h-2) * (w-2) == yellow:
                return [w,h]



print("답: ",solution(24,	24	)) 