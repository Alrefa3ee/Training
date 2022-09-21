# Worng answer

import typing as t


c = 5  # عدد الخلاية الكلي
n = [1, 1, 0, 1, 0]  # حالة الخلاية
k = 3  # عدد الدورات

n = [bool(i) for i in n] * k  # تكرار الدورات

steps = 0
position = 0
for i in range(k):
    n[position+2:4] = [False for i in n[position+2:4]]
    n[position+4] = True
    position += 3

# print([int(i) for i in n[]])
print([int(i) for i in n])
