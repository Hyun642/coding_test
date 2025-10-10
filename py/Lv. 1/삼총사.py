def solution(number):
    answer = 0
    for i in range(len(number)):
        if i>2:
            break
        for j in range(i+1,len(number)):
            
            for k in range(j+1,len(number)):
                if(number[i]+number[j]+number[k] == 0):
                    answer += 1
    
    return answer

print(solution([-3, -2, -1, 0, 1, 2, 3]	))
print(solution([-2, 3, 0, 2, -5]	))