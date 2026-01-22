def solution(s):
    stack=[]
    for x in (s):
        if stack and stack[-1] == x:
            stack.pop() 
        else:
            stack.append(x)
    return 1 if not stack else 0

print("답: ",solution("baabaa"		)) 
#	1
print("답: ",solution("cdcd")) 
#   0