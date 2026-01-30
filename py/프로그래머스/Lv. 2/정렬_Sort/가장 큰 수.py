def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x:x*3,reverse=True)       
    answer= ''.join(numbers)
    return str(int(answer))
print("답: ",solution(	[6, 10, 2]))
print("답: ",solution(	[3, 30, 34, 5, 9]))
print("답: ",solution(	[0,0]))

