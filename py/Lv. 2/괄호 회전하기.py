import collections 
def solution(s):
    answer = 0
    q= collections.deque(s)
    for i in range(len(s)):
        stack = []
        yes=True
        for i in q:
            if i in '({[':
                stack.append(i)
            else:
                if stack:
                    if i == ')' and stack[-1] == '(':
                            stack.pop()
                    elif i == '}'and stack[-1] == '{':
                            stack.pop()
                    elif i == ']'and stack[-1] == '[':
                            stack.pop()
                    else: yes=False
                else: 
                    yes=False
                    break
        if not stack and yes:
            answer+=1
        q.rotate()

    return answer

print("답: ",solution("[](){}")) 