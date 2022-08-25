# Python Interview
# Array Partition / p.190
# parameter ls: list[int]
# return: int

def solution_by_descending_order(ls):
    return sum(sorted(ls)[::2])
