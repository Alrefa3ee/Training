import typing as t

c = 4
positios = [(5, 2), (8, 7), (6, 3), (4, 4)]

result: t.List[bool] = []
for position, v in enumerate(positios):
    row, col = v[0], v[1]
    x = list(filter(lambda x: x != v, positios))
    result.append(False in [(row == r or col == c) for r, c in x])

if False in result:
    print("Not safe")
else:
    print("Safe")
