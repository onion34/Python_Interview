# Python Interview
# Trapping Rain Water / p.180
# parameter height: list[int]
# return: int

def solution_by_pointer(height):
    if not height:
        return 0

    result = 0
    cur_l, cur_r = 0, len(height) - 1
    l_max, r_max = height[cur_l], height[cur_r]

    while cur_l < cur_r:
        l_max, r_max = max(l_max, height[cur_l]), max(r_max, height[cur_r])

        if l_max <= r_max:
            result += l_max - height[cur_l]
            cur_l += 1

        else:
            result += r_max - height[cur_r]
            cur_r -= 1

    return result
