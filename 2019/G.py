import math
n  = 3 # عدد الكتب في المعرض
p = 10 #المبلغ المالي المحدد 

h = [2,6,3] # سعر كل كتاب 
s = [8,5,4] # عدد صفحات كل كتاب
k = [3,5,2] # عدد النسخ من كل كتاب


# طباعة أكبر عدد من الصفحات التي يمكن شرائها

all = list(zip(h,s,k))

def higher_price_for_book(l:list):
    for i in range(len(l)):
        price = l[i][0]*l[i][-1]
        pages = l[i][1]*l[i][-1]
        if price ==p:
            print(price,pages,i)
        else:
            pass
            

higher_price_for_book(all)