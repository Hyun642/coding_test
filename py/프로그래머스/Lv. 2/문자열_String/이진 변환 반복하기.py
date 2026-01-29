def solution(s):
    i=0
    zero=0
    while s != "1":
        zero += s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]
        i+=1
    return [i,zero]


print("답: ",solution("110010101001"	)) 
#[3,8]
# print("답: ",solution("1111111"	)) 
#[4,1]