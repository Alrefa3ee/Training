text = "Mathematician"

steps = 0
while steps < len(text):
    if text[:steps] != "":
        print(" ".join(text[:steps]))
    text =  text.replace(text[:steps], "", 1)
    steps += 1

print(" ".join(text[:steps]))
