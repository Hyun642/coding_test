def solution(s):
    answer = []
    n= 0
    for i in (s):
        if i == ' ':
            n=0
            answer.append(' ')
        elif n%2 == 0:
            answer.append(i.upper())
            n+=1
        else:
            answer.append(i.lower())
            n+=1
    
    return    ''.join(answer)

print(solution("try hello world"	))