def solution(n):
    temp = [n]
    nums = n

    while nums != 1:
        if nums % 2 == 0:
            nums = nums // 2
        else:
            nums = 3 * nums + 1

        temp.append(nums)

    return temp

        