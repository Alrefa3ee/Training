L = 10
D = 2
S = 1

def day_count(L: int, D: int, S: int, k: int = 0, days: int = 0) -> int:
    k += D
    days += 1
    if k == L:
        return days
    k -= S
    return day_count(L, D, S, k, days)

print(day_count(L, D, S))
