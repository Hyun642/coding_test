def solution(n):
    n_count = bin(n).count("1")
    while True:
        n+=1
        if bin(n).count("1") == n_count:
            return n
       

print("답: ",solution(78	)) 
#	83
# print("답: ",solution()) 
#