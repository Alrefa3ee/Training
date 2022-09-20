import typing as t

numbers = {
    "4": "IV",
    "9": "IX",
    "40": "XL",
    "90": "XC",
    "400": "CD",
    "900": "CM",
    "1": "I",
    "5": "V",
    "7": "VII",
    "10": "X",
    "50": "L",
    "100": "C",
    "500": "D",
    "1000": "M",
    "2000": "MM"
}

def get_pos_nums(num: str, c: int = 1, pos_nums: t.List[int] = []) -> t.List[int]:
    num = int(num)
    if num != 0:
        z = num % 10
        pos_nums.append(z *c)
        num = num // 10
        c = c*10
        return get_pos_nums(str(num), c, pos_nums)
    pos_nums.reverse()
    return pos_nums

def romanize(num: str) -> str:
    return "".join([numbers[str(n)] for n in get_pos_nums(num)])

x = romanize("1955")
print(x)
