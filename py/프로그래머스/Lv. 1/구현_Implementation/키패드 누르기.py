def solution(numbers, hand):
    answer = ''
    dic={
        1:[0,0],2:[0,1],3:[0,2],
        4:[1,0],5:[1,1],6:[1,2],
        7:[2,0],8:[2,1],9:[2,2],
        "*":[3,0],0:[3,1],"#":[3,2]
    }
    
    left_now =   [3,0]
    right_now =  [3,2]

    for i in numbers:
        if i in [1,4,7]:
            left_now = dic[i]
            answer += "L"
        elif i in [3,6,9]:
            right_now = dic[i]
            answer += "R"
        else:
            now_index = dic[i]
            l_dis= abs(now_index[0]-left_now[0])+abs(now_index[1]-left_now[1])
            r_dis= abs(now_index[0]-right_now[0])+abs(now_index[1]-right_now[1])
            if l_dis < r_dis:
                answer +='L'
                left_now = dic[i]
            elif l_dis > r_dis:
                answer +='R'
                right_now = dic[i]
            else:
                if hand =='right':
                    answer += 'R'
                    right_now = dic[i]  
                else:
                    answer += 'L'
                    left_now = dic[i]  

    return answer



print( solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right"))#"LRLLLRLLRRL"



