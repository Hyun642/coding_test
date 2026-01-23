import collections 
def solution(str1, str2):
    s=[]
    s2=[]

    for x in range(0,len(str1)-1):
        if str1[x:x+2].isalpha():
            s.append(str1[x:x+2].lower())
    for x in range(0,len(str2)-1):
        if str2[x:x+2].isalpha():
            s2.append(str2[x:x+2].lower())

    if not s and not s2:
        return 65536 

    dic = collections.Counter(s)
    dic2 = collections.Counter(s2)

    union = sum((dic | dic2).values())
    inter = sum((dic & dic2).values())

    
    return int(inter/union *65536)

print("답: ",solution("FRANCE",	"french"))
print("답: ",solution("handshake",	"shake hands"))
print("답: ",solution("aa1+aa2",	"AAAA12"))
print("답: ",solution("E=M*C^2",	"e=m*c^2"))