# Python Interview
# Product of Array Except Self / p.193
# parameter ls: list[int]
# return: list[int]

def solution(ls):
    result = []
    p = 1

    for i in range(len(ls)):
        result.append(p)
        p *= ls[i]

    p = 1
    for i in range(len(ls)-1, -1, -1):
        result[i] *= p
        p *= ls[i]

    return result


# 매우 비효율적 reduce 함수의 사용만 알고 간다
def solution_by_reduce(ls):
    from functools import reduce

    result = []

    for i in range(len(ls)):
        result.append(reduce(lambda x, y: x * y, ls[:i] + ls[i+1:]))

    return result
