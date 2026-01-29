def solution(answers):
    a=[1, 2, 3, 4, 5]
    b=[2, 1, 2, 3, 2, 4, 2, 5]
    c=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score=[0,0,0]

    for i,x in enumerate(answers):
        if x==a[i%len(a)]:
            score[0]+=1
        if x==b[i%len(b)]:
            score[1]+=1
        if x==c[i%len(c)]:
            score[2]+=1
    
    max_score=max(score)

    result=[]
    for i,x in enumerate(score):
        if max_score == x:
            result.append(i+1)

    return result


print("답: ",solution([1,2,3,4,5]))
print("답: ",solution([1,3,2,4,2]))