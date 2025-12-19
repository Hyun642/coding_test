def solution(s):
    answer = []
    memo = {}
    for i,char in enumerate(s):
        if char in memo:
            answer.append(i-memo[char])
        else: 
            answer.append(-1)
        memo[char] = i
    return answer
