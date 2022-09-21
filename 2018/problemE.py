numbers = []

x = {
    "A": lambda x, y: x + y,
    "S": lambda x, y: x - y,
    "M": lambda x, y: x * y,
    "D": lambda x, y: x / y,
    "P": numbers.append,
    "R": None
}

def main() -> int:
    global numbers
    operation = str(input(""))
    if operation == "R":
        return int(numbers[-1])
    elif operation.startswith("P"):
        numbers.append(int(operation.split(" ")[1]))
        return main()
    else:
        result = x[operation](numbers[-2], numbers[-1])
        numbers[-1] = result
        return main()

print(main())
