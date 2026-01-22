import sys

input = sys.stdin.readline
n = int(input())

count= 1
sum = 1
step=6
while n >  sum:
    sum += step
    step+=6
    count +=1
print(count)

