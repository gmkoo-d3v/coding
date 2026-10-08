def solution(a, b, c, d):
    temp = [a, b, c, d]
    count = {}
    
    for nums in temp:
        count[nums] = count.get(nums,0) + 1
    
    if len(count) == 1:
        p = next(iter(count))
        return 1111*p
    
    elif len(count) == 2:
        nums = list(count.keys())
        
        p = nums[0]
        q = nums[1]
    
        if count[p] == 3:
            return (10 * p + q) ** 2
        
        elif count[q] == 3:
            return (10 * q + p) ** 2
        
        else:
            return (p + q) * abs(p-q)
        
    elif len(count) == 3:
        p = 0
        others = []
        
        for numbs, value in count.items():
            if value == 2:
                p = numbs
            else: others.append(numbs)
        
        q, r = others
        return q * r
    
    else:
        return min(temp)
            