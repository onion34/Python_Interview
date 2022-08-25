# Python Interview
# Group Anagram / p.153

def solution(ls: list[str]) -> list[list[str]]:
    from collections import defaultdict
    
    anagram = defaultdict(list)
    
    for word in ls:
        anagram[''.join(sorted(word))].append(word)
    
    return list(anagram.values())
