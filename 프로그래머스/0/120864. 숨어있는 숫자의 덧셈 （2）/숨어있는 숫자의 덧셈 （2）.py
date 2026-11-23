def solution(my_string):

    total = 0
    current = 0
    number = False
    
    for ch in my_string:
        if ch.isdigit():
            current = current * 10 + int(ch)
            number = True
        else:
            if number:
                total += current
                current = 0
                number = False
    if number:
        total += current
    
    return total