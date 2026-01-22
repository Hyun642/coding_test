def solution(ingredient):
    answer = 0
    stock=[]
    i=0

    for i in ingredient:
        stock.append(i)
        if len(stock) >= 4 and stock[-4:] == [1,2,3,1]:
            stock.pop()
            stock.pop()
            stock.pop()
            stock.pop()
            answer+=1
    return answer

print("답: ",solution([2, 1, 1, 2, 3, 1, 2, 3, 1]		))
print("답: ",solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))