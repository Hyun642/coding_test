def solution(elements):
    answer = set()
    elements += elements
    for i in range(len(elements)//2):
        hap = 0
        for j in range(len(elements)//2):
            answer.add(sum(elements[j:(j+i+1)]))


    return len(answer)


print("답: ",solution([7,9,1,1,4]	))