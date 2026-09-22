import math
def solution(price):
    total = price
    if price >= 500000:
        total *= 0.80
    elif price >= 300000:
        total *= 0.90
    elif price >= 100000:
        total *= 0.95
    return math.floor(total)