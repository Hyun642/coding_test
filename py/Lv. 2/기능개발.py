def solution(progresses, speeds):
    answer = []

    max_day = 0
    for i,j in zip(progresses,speeds):
        day= 0
        if ((100-i) % j > 0):
            day=((100-i) // j+1)
        else:
            day=((100-i) // j)


        if day > max_day:
            answer.append(1)
            max_day = day
        else:
            answer[-1] += 1
    return answer

print(solution([93, 30, 55],	[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]))