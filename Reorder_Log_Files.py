# Python Interview
# Reorder Log Files / p.148

def solution(logs: list[str]) -> list[str]:

    letter_log = []
    digit_log = []

    for log in logs:

        digit_log.append(log) if log.split()[1].isdigit() else letter_log.append(log)

    letter_log.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    
    return letter_log + digit_log
