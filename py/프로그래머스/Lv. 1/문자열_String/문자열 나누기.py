def solution(s):
    answer=0
    len_a=0
    len_b=0
    x=""
    for char in (s):
        if len_a == 0:
            x=char
            len_a = 1
        else:
            if char == x:
                len_a += 1
            else:
                len_b += 1
    
        if len_a == len_b:
            answer += 1
            len_a=0
            len_b=0
    if len_a > 0:
        answer += 1 
    return answer

print( solution("banana"))
print( solution("abracadabra"))



