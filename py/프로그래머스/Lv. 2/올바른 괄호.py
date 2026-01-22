def solution(s):
    stack =[]
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                 return False
            stack.pop()


    return len(stack) == 0

# print(solution("()()"))
print(solution("(()("))