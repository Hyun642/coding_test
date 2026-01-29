import collections
def solution(want, number, discount):
    answer = 0
    dic = collections.defaultdict()
    for x,y in zip(want,number):
        dic[x] = y

    for i in range(len(discount)-9):
        cur_10_days = collections.Counter(discount[i:i+10])
        if cur_10_days == dic:
            answer+=1

    return answer


print("답: ",solution(["banana", "apple", "rice", "pork", "pot"],	[3, 2, 2, 2, 1],	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))