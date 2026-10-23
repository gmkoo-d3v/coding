def solution(s):
    countp = 0
    county = 0
    
    s = s.lower()
    for i in range(len(s)):
        if s[i] == 'p':
            countp +=1
        elif s[i] == 'y':
            county +=1
        else:
            continue
    if countp == county: return True
    else: return False