def solution(keymap, targets):
    answer = [] 
    min_press={}

    for keys in keymap:
        for i,char in enumerate(keys):
            count = i + 1
            if char not in min_press or count < min_press[char]:
                min_press[char] = count
    
    for target in targets:
        total_clicked=0
        searched = True
        for char in target:
            if char in min_press:
                total_clicked+=min_press[char]
            else:
                searched = False
                break
        answer.append(total_clicked if searched else -1)

    return answer

print("답: ",solution(["ABACD", "BCEFD"],	["ABCD","AABB"]	))
print("답: ",solution(["AA"],	["B"]))
print("답: ",solution(["AGZ", "BSSS"],	["ASA","BGZ"]	))