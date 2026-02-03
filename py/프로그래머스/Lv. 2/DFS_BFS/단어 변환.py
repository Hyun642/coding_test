from collections import deque 

def solution(begin, target, words):
    visited = set()
    que = deque([(begin,0)])
    if target not in words:
        return 0
    
    
    while que:
        cur_word,steps = que.popleft()
        
        if cur_word == target:
            return steps
        
        for word in words:
            if word not in visited:
                df=0
                for i in range(len(cur_word)):
                    if cur_word[i] != word[i]:
                        df+=1

                if df == 1:
                    que.append((word,steps+1))
                    visited.add(word)
    return 0

print("답: ",solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]	))
# print("답: ",solution("I"	   ))