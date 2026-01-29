def solution(skill, skill_trees):
    answer = 0
    dic = {x:i for i,x in enumerate(skill)}
    for i in skill_trees:
        li = ""
        for j in i:
            if j in dic:
                li+=j
        for word in range(len(li)):
            if dic[li[word]] != word:
                break
        else:
            answer+=1
    return answer

print("답: ",solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]		))