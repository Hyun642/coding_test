def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name,yearning))

    for k in photo:
        sum =0
        for l in k:
            if l in dic:
                sum += dic[l]
        answer.append(sum)
    return answer



print("답: ",solution(["may", "kein", "kain", "radi"],	[5, 10, 1, 3],	[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]] ))