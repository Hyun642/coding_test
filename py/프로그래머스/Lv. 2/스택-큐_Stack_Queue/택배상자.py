def solution(order):
    stack=[]
    idx=0
    n=len(order)

    for box in range(1,n+1):
        stack.append(box)

        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
    return idx


print("답: ",solution([4, 3, 1, 2, 5]))
print("답: ",solution([5, 4, 3, 2, 1]))