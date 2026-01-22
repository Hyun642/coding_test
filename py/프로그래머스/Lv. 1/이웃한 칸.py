def solution(board,	h,	w):
    main_color = board[h][w]
    count = 0
    max_length = len(board)
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    for i in range(4):
        h_check= h+dh[i]
        w_check= w+dw[i]
        if 0 <= h_check <  max_length and 0 <= w_check <  max_length:
            if main_color == board[h_check][w_check]:
                count+=1
                
    return count


print( solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]],	1,	1))
print( solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]],	0,	1))