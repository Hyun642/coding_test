def solution(babbling):
    answer = 0
    for word in (babbling):
        is_valid = True
        for s in ['aya', 'ye','woo','ma']:
            if s*2 in word:
                is_valid=False
                break
            else:
                word = word.replace(s," ")
        if is_valid and word.strip() =="":
            answer +=1
    return answer


print("답: ",solution(["aya", "yee", "u", "maa"]))
print("답: ",solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))