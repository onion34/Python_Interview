# Python Interview
# Two Sum / p.173
# parameter ls: list[int], targer: int
# return: list[int]

def solution_by_brute_force(ls, target):

    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            if ls[i] + ls[j] == target:
                return [i, j]


def solution_by_in(ls, target):

    for idx, num in enumerate(ls):
        cur_cmp = target - num

        if cur_cmp in ls[idx+1:]:
            return [idx, ls[idx+1:].index(cur_cmp) + (idx + 1)]


def solution_by_dict(ls, target):
    num_dict = {}

    for idx, num in enumerate(ls):
        num_dict[num] = idx

    for idx, num in enumerate(ls):
        if target - num in num_dict and idx != num_dict[target - num]:
            return [idx, num_dict[target - num]]


def solution_by_improved_dict(ls, target):
    num_dict = {}

    for idx, num in enumerate(ls):
        if target - num in num_dict:
            return [idx, num_dict[target - num]]

        num_dict[num] = idx
