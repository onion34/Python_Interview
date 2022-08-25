# Python Interview
# 3Sum / p.184
# parameter ls: list[int]
# return: list[list[int]]

def solution_by_brute_force(ls):
    result = []
    ls.sort()

    for i in range(len(ls) - 2):
        if i > 0 and ls[i] == ls[i - 1]:
            continue

        for j in range(i + 1, len(ls) - 1):
            if j > i + 1 and ls[j] == ls[j - 1]:
                continue

            for k in range(j + 1, len(ls)):
                if k > j + 1 and ls[k] == ls[k - 1]:
                    continue

                if ls[i] + ls[j] + ls[k] == 0:
                    result.append([ls[i], ls[j], ls[k]])

    return result


def solution_by_pointer(ls):
    result = []
    ls.sort()

    for i in range(len(ls) - 2):
        if i > 0 and ls[i] == ls[i-1]:
            continue

        left, right = i + 1, len(ls) - 1

        while left < right:
            value = ls[i] + ls[left] + ls[right]

            if value < 0:
                left += 1

            elif value > 0:
                right -= 1

            else:
                result.append([ls[i], ls[left], ls[right]])

                while left < right and ls[left] == ls[left + 1]:
                    left += 1

                while left < right and ls[right] == ls[right - 1]:
                    right -= 1

                left += 1
                right -= 1
    
    return result
