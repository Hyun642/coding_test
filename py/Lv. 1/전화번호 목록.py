def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for i,j in zip(phoneBook,phoneBook[1:]):
            if j.startswith(i):
                return False
    return True


# print(solution(	["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
# print(solution(["12", "123", "1235", "567", "88"]))
