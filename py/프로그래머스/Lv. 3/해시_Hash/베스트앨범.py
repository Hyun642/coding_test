def solution(genres, plays):
    answer=[]
    genres_sum = dict()
    genres_info = dict()
    for i in range(len(genres)):
        if genres[i] in genres_sum: genres_sum[genres[i]] += plays[i]
        else: genres_sum[genres[i]] = plays[i]
        
        if genres[i] in genres_info: genres_info[genres[i]].append([i,plays[i]])
        else: genres_info[genres[i]] = [[i,plays[i]]]

    for (k,v) in sorted(list(genres_sum.items()), key=lambda x:-x[1]):
        count = 0
        for i,j in (sorted(list(genres_info[k]),key=lambda y:-y[1])):
            answer.append(i)
            count +=1
            if count >= 2:
                break
    return answer
#

print(solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]))