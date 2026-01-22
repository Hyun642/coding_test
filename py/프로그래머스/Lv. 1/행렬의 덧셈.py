def solution(arr1, arr2	):
    return [[c1+c2 for c1,c2 in zip(i,j)] for i,j in zip(arr1,arr2)]

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]],	[[3],[4]]))

