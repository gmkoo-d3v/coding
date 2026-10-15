def solution(arr):
    total = 0
    length = len(arr)
    for i in arr:
        total += i
    total /=length
    return total