def solution(wallet, bill):
    answer = 0

    while max(wallet) < max(bill) or min(wallet) < min(bill):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer+=1

    return answer


print("답: ",solution([30, 15],	[26, 17]	))
print("답: ",solution([50, 50],	[100, 241]	))