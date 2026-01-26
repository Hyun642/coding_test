def solution(numbers):
    stack=[]
    answer=[-1] * len(numbers)
    for index,num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            last_index= stack.pop()
            answer[last_index] = num
        stack.append(index)
    return answer

print("답: ",solution([8, 1, 2, 9]))
print("답: ",solution([2, 3, 3, 5]	))