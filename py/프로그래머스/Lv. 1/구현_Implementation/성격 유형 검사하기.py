def solution(survey, choices):
    dic={"RT":[0,0],"CF":[0,0],"JM":[0,0],"AN":[0,0]}
    answer = ""

    for choice,question in zip(choices,survey):
        point = 4-choice

        if question in dic:
            if point > 0:
                dic[question][0] += abs(point)
            else:
                dic[question][1] += abs(point)
            
        else: 
            if point < 0:
                dic[question[-1::-1]][0] += abs(point)
            else:
                dic[question[-1::-1]][1] += abs(point)


    for i in dic:
        if dic[i][0] == dic[i][1]:
            answer += (i[0])
        else:
            answer += (i[dic[i].index(max(dic[i]))])

    return answer

print( solution(["AN", "CF", "MJ", "RT", "NA"],	[5, 3, 2, 7, 5])) 
print( solution(["TR", "RT", "TR"],	[7, 1, 3]))



