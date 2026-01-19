def solution(s):
    answer = []
    s = s.replace('{','[').replace('}',']')

    for i in sorted(eval(s), key=lambda x:len(x)):
        for j in i:
            if j not in answer:
              answer.append(j)

    return answer



print("답: ",solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))