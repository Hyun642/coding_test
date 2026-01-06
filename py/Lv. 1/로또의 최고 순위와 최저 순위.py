def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    zero_count=lottos.count(0)
    if zero_count == 6:
        return [1,6]
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    return [rank[count+zero_count], rank[count]]

print( solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]))
print( solution([0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]))
print( solution([1, 2, 3, 4, 5, 6],	[7, 8, 9, 10, 11, 12]))
