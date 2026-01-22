def solution(s):
    dic = {
        0:	"zero",
        1:	"one",
        2:	"two",
        3:	"three",
        4:	"four",
        5:	"five",
        6:	"six",
        7:	"seven",
        8:	"eight",
        9:	"nine",
    }

    for i,j in dic.items():
        if (j in s):
            s= s.replace(j,str(i))

    return int(s)

print("답: ",solution("one4seveneight"))
# print("답: ",solution("123"	))