def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        count=0
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                if j*j == i:
                    count+=1
                else:      
                    count+=2
        
        if count > limit:
            answer += power
        else:
            answer += count

    return answer











print("답: ",solution(5,	3,	2))
print("답: ",solution(10,	3,	2))