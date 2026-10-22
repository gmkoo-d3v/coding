def solution(pb):
    pb.sort()

    for idx, phone in enumerate(pb[:-1]):
        if pb[idx + 1].startswith(phone):
            return False

    return True