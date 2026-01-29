def solution(dirs):
   
    dic={"U":(0,1),"D":(0,-1),"R":(1,0),"L":(-1,0)}

    x,y = 0,0
    box = set()

    for i in dirs:
        dx,dy= dic[i][0] + x ,dic[i][1] + y

        if -5 <= dx <= 5 and -5 <= dy <= 5:
            box.add((x,y,dx,dy))
            box.add((dx,dy,x,y))
            x,y = dx,dy

    return len(box)//2

print("답: ",solution("ULURRDLLU"))
print("답: ",solution("LULLLLLLU"))