def solution(data,	ext,	val_extm,	sort_by):
    dic={"code":0, "date":1, "maximum":2, "remain":3}
    answer = []


    for d in data:
        if d[dic[ext]]< val_extm:
            answer.append(d)
    
    return sorted(answer, key=lambda x:x[dic[sort_by]])


print( solution([[1, 20300104, 100, 80], 
                 [2, 20300804, 847, 37], 
                 [3, 20300401, 10, 8]],	
                 "date",	20300501,	"remain"	))



