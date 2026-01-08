def solution(today, terms, privacies):
    answer = []
    dic = {}
    for i in terms:
        a,b = i.split(' ')
        dic[a] = int(b)

    오늘날짜=today.split('.')
    for i,date in enumerate(privacies):
        날짜, 조건 = date.split(' ')
        계약날짜=날짜.split('.')
        오늘일=([int(i) for i in 오늘날짜])
        계약일=([int(i) for i in 계약날짜])
        
        오늘일[0] = 오늘일[0] * 12 * 28
        오늘일[1] = 오늘일[1] * 28
        계약일[0] = 계약일[0] * 12 * 28
        계약일[1] = 계약일[1] * 28
        계약일.append(dic[조건] * 28) 

        오늘 = sum(오늘일)
        만료 = sum(계약일)

        print(오늘,만료)

        if 오늘 >= 만료:
            answer.append(i+1)  

    return answer


print("답: ",solution("2022.05.19",	["A 6", "B 12", "C 3"],	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))#[0, 1, 3, 4]
print("답: ",solution("2020.01.01",	["Z 3", "D 5"],	["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))#[0, 1, 3, 4]