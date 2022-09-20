import typing as t

n = 5
k = 1
c = [1, 3]


paper = n * 10

for i in c:
    u = int(n / i)
    paper -= u

print(paper)
