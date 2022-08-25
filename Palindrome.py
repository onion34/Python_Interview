# Python Interview
# Palindrome

def solution_by_list(text: str) -> bool:
    ls = []
    for s in text:
        if s.isalnum():
            ls.append(s.lower())

    while len(ls) > 1:
        if ls.pop(0) != ls.pop():
            return False

    return True


def solution_by_deque(text: str) -> bool:
    from collections import deque

    dq = deque()
    for s in text:
        if s.isalnum():
            dq.append(s.lower())

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True


def solution_by_slicing(text: str) -> bool:
    import re

    text = re.sub(r'\W', '', text.lower())

    return text == text[::-1]
