A_N = "9:00 9:40 9:50 11:00 15:00 18:00"
D_N = "9:10 12:00 11:20 11:30 19:00 20:00"

A = A_N.split(" ")
D = D_N.split(" ")

def time_parser(time: str) -> int:
    hours, minutes = time.split(":")
    return int(hours) * 60 + int(minutes)

def gateways_count(A: t.List[str], D: t.List[str], counter: int = 0) -> int:
    if len(A) == 0 or len(D) == 0:
        return counter
    values = [i for i in A if time_parser(i) <= time_parser(D[0])]
    for value in values:
        A.remove(value)
        D.remove(D[0])
    counter += 1
    return gateways_count(A, D, counter)

print(gateways_count(A, D))
