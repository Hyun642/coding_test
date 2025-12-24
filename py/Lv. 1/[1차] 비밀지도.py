def solution(n, arr1, arr2):
    answer=[]
    for a,b in zip(arr1,arr2):
        com= (bin(a|b)[2:].zfill(n))
        row = com.replace('1','#').replace('0',' ')
        answer.append(row)

    return answer

print("답: ",solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print("답: ",solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10] ))