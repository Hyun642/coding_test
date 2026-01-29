import re

def solution(files):
    parsed=[]
    for file in files:
        
        s= re.split('(\d+)',file)
        parsed.append((s[0].lower(),int(s[1]),file))
    parsed.sort(key=lambda x: (x[0],x[1]))

    return [x[2] for x in parsed]


print("답: ",solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]




