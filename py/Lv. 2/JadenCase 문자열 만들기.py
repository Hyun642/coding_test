def solution(s):
    answer = []

    s = s.split(' ')
    for j in s:

        new_word=''
        for i,me in enumerate(j):
            if i == 0:
                new_word += me.upper()
            else:
                new_word += me.lower()
        answer.append(new_word)
    return ' '.join(answer)





print("답: ",solution("3people unFollowed me")) 
#"3people Unfollowed Me"
print("답: ",solution("for the last week"	)) 
#"For The Last Week"