C_N = input(">>> ")

N = [i for i in range(1, int(C_N.split(" ")[0])+1)]
C = int(C_N.split(" ")[1])

requests = [int(i) for i in input(">>> ").split(" ")]

result = {i: 0 for i in range(1, len(N) + 1)}

keys = []

for i in requests:
    min_num = min(list(result.values()))
    key = [k for k, v in result.items() if v == min_num][0]
    result[key] += i
    keys.append(key)

print(" ".join(map(str, keys)))
