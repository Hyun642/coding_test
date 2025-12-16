from collections  import Counter
def solution(participant, completion):
    p = Counter(participant)    
    c = Counter(completion)    
    return list((p-c).keys())[0]

print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(	["leo", "kiki", "eden"],	["eden", "kiki"]))