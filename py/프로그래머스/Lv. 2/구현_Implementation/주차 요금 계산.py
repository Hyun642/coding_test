from collections import defaultdict
import math
def solution(fees, records):
    basic_fee_time =fees[0]
    basic_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]

    parking_log = defaultdict(list)
    for i in records:
        (time,car_num,state )= i.split(' ')
        m,s = map(int, time.split(':'))
        parking_log[car_num].append(m * 60 + s)

    total_times = defaultdict(int)
    for car,times in parking_log.items():
        if len(times) % 2 != 0:
            times.append(23* 60 + 59)

        for i in range(0,len(times),2):
            total_times[car] += times[i+1]-times[i]
    
    res=[]
    for car in sorted(total_times.keys()):
        time = total_times[car]

        if time <= basic_fee_time:
            fee = basic_fee
        else:
            fee = basic_fee + math.ceil((time - basic_fee_time)/per_time) * per_fee
        res.append(fee)
    return res

print("답: ",solution([120, 0, 60, 591],	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	))
# print("답: ",solution([1, 461, 1, 10],	["00:00 1234 IN","00:10 1234 IN"]		))





