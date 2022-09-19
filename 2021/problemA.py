from BS import binary_search as search
import time 
def find_house(num,house):
    houses = [*range(1,num*2+1)]
    print(houses)
    right = [x for x in houses if x %2 ==0]
    left = [x for x in houses if x %2 !=0]
    return right[-search(left,house)-1]

start = time.time()
print(find_house(3,3))

print(time.time()-start)