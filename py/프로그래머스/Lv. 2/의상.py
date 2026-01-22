from collections import Counter
def solution(clothes):
    counts= Counter([category for x,category in clothes ])
    total=1
    for i in (counts.values()):
        total*=i+1
    return total-1