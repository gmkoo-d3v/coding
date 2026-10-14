def solution(s):
    
    if len(s) != 4 and len(s) != 6:
        return False
    
    try:
        temp = int(s)
        return True
    except ValueError:
        return False
    
        