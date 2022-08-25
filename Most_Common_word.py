# Python Interview
# Most Common Word

def solution(paragraph: str, banned: list[str]) -> str:
    from collections import Counter
    import re

    words_ls = [word for word in re.sub(r'\W', ' ', paragraph)
                .lower().split() if word not in banned]

    return Counter(words_ls).most_common()[0][0]
