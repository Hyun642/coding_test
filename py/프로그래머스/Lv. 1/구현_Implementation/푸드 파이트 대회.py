def solution(food):
    answer = ''
    for i,x in enumerate(food):
            answer+= str(i) * ((x-1)//2)
    return answer + '0' + answer[::-1]

# 0번은 늘 가운데 3446661
# 1번~ 부터는 홀수면 - 1 한다음에 양 옆으로 데칼코마니
# 즉 한쪽만 다 채우고 0 붙이고 데칼코마니

print("답: ",solution([1, 3, 4, 6]))
print("답: ",solution([1, 7, 1, 2]	))