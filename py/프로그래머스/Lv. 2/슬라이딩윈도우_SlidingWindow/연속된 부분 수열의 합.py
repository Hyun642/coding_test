def solution(sequence, k):
    answer=[]
    n = len(sequence)
    start,end = 0,0
    current_sum = sequence[0]
    min_length = n + 1

    while end < n:
        if current_sum == k:
            current_length = end - start
            #더 짧은 수열을 찾았을 때
            if current_length < min_length:
                min_length = current_length
                answer = [start,end]
            #다음 구간을 찾기 위해 한 칸 이동
            current_sum -= sequence[start]
            start += 1
        
        elif current_sum < k:
            end += 1
            if end < n:
                current_sum += sequence[end]
        else:
            current_sum -= sequence[start]
            start +=1 



    return answer

print("답: ",solution( [1, 2, 3, 4, 5],	7   ))
print("답: ",solution( [2, 2, 2, 2, 2],	6	   ))