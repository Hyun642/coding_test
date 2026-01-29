import collections

def solution(record):
    answer = []
    #record를 뒤에서부터 정렬
    #회원명 업데이트 용 id:name
    name_list=collections.defaultdict(str)
    new_record=[]
    #새로운 id가 나올떄마다 new_record = [(id, enter)] 저장 
    for i in record:
        i = i.split(' ')
        command,uid = i[0],i[1]
        if len(i) == 3:   
            name_list[uid] = i[2]
        if command in ('Enter','Leave'):
            new_record.append((uid,command)) 

    #새로운 반복문
    # new_record 순서대로 id로 이름 뽑고 enter 여부 확인
    for uid,command in new_record:
        last_name = name_list[uid] 
        if command == 'Enter':
            answer.append(f'{last_name}님이 들어왔습니다.')
        elif command =='Leave':
            answer.append(f'{last_name}님이 나갔습니다.')
    return answer

print("답: ",solution( ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))


