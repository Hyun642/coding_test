import itertools

def solution(s):
    answer = 0
    a= itertools.combinations(s,3)
    for k in ((a)):
        v= sum(k)
        b=0
        for i in range(1,int(v**0.5)+1):
            if v%i == 0:
                b+=1
        if b == 1:
            answer+=1

    return answer