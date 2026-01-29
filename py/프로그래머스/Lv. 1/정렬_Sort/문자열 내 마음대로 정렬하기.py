def solution(strings,	n):
    return sorted(strings, key=lambda x:(x[n],x))


print("답: ",solution(["sun", "bed", "car"],	1))
print("답: ",solution(["abce", "abcd", "cdx"],	2))