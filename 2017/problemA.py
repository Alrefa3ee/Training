text = "DRINKEATCODEB"

literals = {"A": 1, "D": 1, "O": 1, "P": 1, "Q": 1, "R": 1, "B": 2}

steps = 0
for char in text.upper():
    if char in literals:
        steps += literals[char]
    else:
        ...

print(steps)
