def solution(arr):
    def compress(r, c, n):
        first_val = arr[r][c]

        for i in range(r,r+n):
            for j in range(c, c+n):
                if arr[i][j] != first_val:
                    half = n//2

                    l1 = compress(r,c, half)
                    l2 = compress(r,c+half, half)
                    l3 = compress(r+half,c, half)
                    l4 = compress(r+half,c+half, half)
                    #마지막 반환
                    return [l1[0]+l2[0]+l3[0]+l4[0],l1[1]+l2[1]+l3[1]+l4[1]]

        if first_val == 0:
            return [1,0]
        else:
            return [0,1]

    return compress(0, 0, len(arr))

# print("답: ",solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	))
print("답: ",solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))