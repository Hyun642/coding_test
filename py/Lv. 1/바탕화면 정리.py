def solution(wallpaper):
    lux, luy, rdx, rdy = len(wallpaper), len(wallpaper[0]),0,0
    for i,x in enumerate(wallpaper):
        
        for j,y in enumerate(wallpaper[i]):
            if y == "#":
                if j < luy:
                    luy = j
                if j > rdy:
                    rdy = j
                if i < lux:
                    lux = i    
                if i > rdx:
                    rdx = i
    
    return  lux, luy, rdx+1, rdy+1


print("답: ",solution([".#...", "..#..", "...#."]))#[0, 1, 3, 4]
print("답: ",solution(["..", "#."]))#[1, 0, 2, 1]