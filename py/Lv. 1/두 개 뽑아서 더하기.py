import itertools
def solution(numbers):
    return sorted(set(a+b for a,b in itertools.combinations(numbers,2))) 

print("답: ",solution([5,0,2,7]))