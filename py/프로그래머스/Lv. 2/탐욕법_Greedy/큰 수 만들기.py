def solution(number, k):
    stack=[]
    count =0
    for index,i in enumerate(number):
        while stack and stack[-1] < i and count < k:
            stack.pop()
            count +=1

        stack.append(i)

        if count ==k:
            break
    slicing = k-count
    return (''.join(stack) + number[index+1:])[:len(number)-slicing]

print("답: ",solution("1924",	2		))
print("답: ",solution("1231234",	3		))
print("답: ",solution("4177252841",	4	))