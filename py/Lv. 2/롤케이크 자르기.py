from collections import Counter
def solution(topping):
    answer=0
    set1= set()
    dic=Counter(topping)
    set2= len(dic)
    
    for i in range(len(topping)):
        set1.add(topping[i])
        dic[topping[i] ] -= 1
        if dic[topping[i]] == 0:
            set2 -= 1

        if len(set1) ==set2:
            answer+=1

    return answer


print("답: ",solution([1, 2, 1, 3, 1, 4, 1, 2]))