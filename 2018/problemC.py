import typing as t

c = 3
names = ["ABBBCCDEAB", "HELLO", "GEEKFORRRRGEEEK"]

def clean_name(name: str) -> str:
    x = ""
    for char in name:
        if x.count(char) > 1: 
            continue 
        else: 
            x += char
    return x

for name in names:
    print(clean_name(name))
