# Python Interview
# The Longest Palindrome Substring // p.159

def solution(text: str):

    if len(text) < 2 or text == text[::-1]:
        return text

    def expand(left_idx: int, right_idx: int) -> str:
        while left_idx >= 0 and right_idx < len(text)-1 and text[left_idx] == text[right_idx]:
            left_idx -= 1
            right_idx += 1
        
        return text[left_idx+1:right_idx]
    
    result = -1
    for i in range(len(text) - 1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    
    return result
