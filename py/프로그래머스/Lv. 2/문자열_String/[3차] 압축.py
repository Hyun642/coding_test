def solution(msg):
    dic = {chr(ord('A') + i): i + 1 for i in range(26)}
    next_index = 27
    answer = []
    
    start = 0

    while start < len(msg)     :
        end = start+1

        while end <= len(msg) and msg[start:end] in dic:
            end+=1
        
        target_word = msg[start:end-1]
        answer.append(dic[target_word])

        if end <= len(msg):
            new_word = msg[start:end]
            dic[new_word] = next_index
            next_index +=1

        start = end - 1

    return answer

print("답: ",solution("KAKAO"))