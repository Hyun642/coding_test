def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    for a in (new_id):
        if a in ["-","_","."] or a.isdigit() or a.islower():
            answer+= a

    while ".." in answer:
        answer = answer.replace("..",'.')

    answer = answer.strip('.')

    if not answer:
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]

    answer = answer.rstrip('.')

    while len(answer) < 3:
        answer += answer[-1]
            
    return answer



print("답: ",solution("...!@BaT#*..y.abcdefghijklm"))#"bat.y.abcdefghi"
# print("답: ",solution("z-+.^."))#"z--"
# print("답: ",solution("=.="))#"aaa"