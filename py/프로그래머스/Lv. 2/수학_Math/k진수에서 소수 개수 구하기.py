def solution(n, k):
    answer=''
    while n > 0:
        answer= str(n%k) + answer
        n//=k


    prime = (answer).split("0")

    prime = list(map(lambda x: int(x) if x.isdigit() else 0, prime))
    
    sum=0
    for i in prime:
        if i < 2: continue
        count =0
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                count+=1
                break
        if count == 0:
            sum+=1
    return sum

print("답: ",solution(437674,	3	))
print("답: ",solution(110011,	10		))