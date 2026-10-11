def solution(sizes):
    max_w, max_h = 0, 0
    
    for i, j in sizes:
        i, j = max(i,j), min(i,j)
        
        max_w = max(max_w,i)
        max_h = max(max_h,j)
    return max_w * max_h