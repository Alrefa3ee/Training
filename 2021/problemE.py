n = int(input("Enter: ").strip()) # strip : ignore the white space in the beginning and the end of the input to avoid errors
# condition
while n > pow(10,5): n = int(input("Enter: ").strip())

steps = int(input("Steps: ").strip()) -1
n = [x+1 for x in range(n)]

# algorithm
i = steps
while len(n) != 1:
    if i > len(n) -1: 
        while i > len(n)-1:
            i = abs(len(n) - i)
        n.pop(i)
        i += steps
    else:
        n.pop(i)
        i += steps

# result
print(n[0])