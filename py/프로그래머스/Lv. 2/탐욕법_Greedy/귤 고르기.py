import collections
def solution(k, tangerine):
    dic=collections.Counter(tangerine)
    answer=0
    total = 0
         
    for _,count in (dic.most_common()):
        total += count
        answer+=1
        if total >= k:
           return answer

print("답: ",solution(6,[1, 3, 2, 5, 4, 5, 2, 3]		)) 
# 3
print("답: ",solution(4,	[1, 3, 2, 5, 4, 5, 2, 3]		)) 
#2
print("답: ",solution(2,[1, 1, 1, 1, 2, 2, 2, 3]		)) 
# 1