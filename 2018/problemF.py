M = 6
N = 3
boxs = [
    [3, 3, 4, 4, 4, 2],
    [3, 1, 3, 2, 1, 4],
    [7, 3, 1, 6, 4, 1]
]

lenght = sum([sum(i) for i in boxs]) / (M * N)

def main():
    min_box = min([min(i) for i in boxs])
    indexs = [[i for i, v in enumerate(box) if v == min_box] for box in boxs]
    result = 0
    for index, i in enumerate(indexs):
        if (i == []) or (i == M-1 or boxs[index][0] == i) or (index == boxs.index(boxs[-1]) or index == boxs[index][0]):
            continue
        for o in i:
            right, left = boxs[index][o+1], boxs[index][o-1]
            top, bottom = boxs[index+1][o], boxs[index-1][o]
            result += int(lenght) - min_box
            for u in [right, left, top, bottom]:
                if u < lenght:
                    result += int(lenght) - u
    return result

result = main()
print(result)
