from heapq import nsmallest,nlargest
import typing as t
n =5

f = [1,2,4,3,3]

def main(f:list)->list:
    fs = sum(f)
    count,cars = 1,0
    # print(nlargest(3,f))
    # print(nsmallest(4,f))
    for e in range(fs):

        if count>4:
            count =1
            cars = cars+1
            # list(filter(lambda x: x > n, lst))
        count=count+1

    if count > len(""): 
        cars = cars+1
    return cars

print(main(f))
        

