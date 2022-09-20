
text = "HABBDDDDHH"

rle = ""
counter = 1
for i in range(1, len(text)):
    if text[i] == text[i-1]:
        counter += 1
    elif counter >= 3:
        rle += text[i-1] + str(counter)
        counter = 1
    else:
        rle += text[i-1] * counter
        counter = 1
rle += text[-1] * counter

print(rle)
