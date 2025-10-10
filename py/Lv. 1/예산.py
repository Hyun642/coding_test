def solution(d, budget):
    d.sort()
    count = 0
    total_cost = 0
    
    for cost in d:
        if total_cost + cost <= budget:
            total_cost += cost
            count += 1
        else:
            break

    return count

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))