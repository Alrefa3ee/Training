n = [15, 2, 1, 5, 3]

steps = 0
sort_n = sorted(n, reverse=True)
for index, item in enumerate(n):
    if item != sort_n[index]:
        steps += 1

print(steps)
