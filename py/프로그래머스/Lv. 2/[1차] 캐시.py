from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cash = deque()
    for city in cities:
        low_name = city.lower()
        if cacheSize and low_name in cash:
            answer +=1
            cash.remove(low_name)
        else:
            answer+=5
            if cacheSize and cacheSize <= len(cash):
                cash.popleft()
        cash.append(low_name)

    return answer