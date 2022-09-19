r = 2
s = [7, 2, 4, 6, 5, 9, 12, 11]


def main(r, s: list):
    groups = []
    for i in range(len(s)):
        if s[i] + r in s and s[i] - r in s:
            groups.append([s[i], s[i] + r, s[i] - r])
        elif s[i] + r not in s and s[i] - r not in s:
            groups.append([s[i]])
    return groups


L = main(2,s)
print([x for x in L[0]if x in L[2]])
for i in range(len(L)):       
    try:
        print([x for x in L[i] if x in L[i+1]])
    except IndexError:
        print([x for x in L[i] if x in L[i]])

def forEach(r):
    pass
# if any element in arry = any element in other arry:
# remove from one

# # Python 3 code to demonstrate
# # removing duplicated from list
# # using list comprehension

# # initializing list
# test = main(r,s)
# # for i in range(len(test)):
# #     print(sorted(test[i]))

# l = [sorted(x) for x in test]

# listToStr = ' '.join([str(elem) for elem in test])

# # for i in range(len(listToStr)):
# #     if listToStr[i] in
# def find(s, ch):
#     return [i for i, ltr in enumerate(s) if ltr == ch]
# f = find(listToStr,"7")
# p = listToStr[:f[1]]
# m = listToStr[f[1]+1:]
# print(p + m)
# # def remove_others(l:list,l2,l3,v:int):
# #     if v in l :
# #         l.remove(v)
# #         l2.remove(v)
# #         l3.remove(v)
# # for i in range(len(test)):
# #     for e in test[i]:
# #         if e not in test:
# #             pass
# #         else:
# #             remove_others(test[i+1],test[i+2],test[i+3],e)

# # print(test)
