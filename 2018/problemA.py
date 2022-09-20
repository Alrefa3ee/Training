import typing as t

n = 15
n_nums = [1, 3, 14, 7]

is_even = lambda x: x % 2 == 0

x = [is_even(i) for i in range(n)]
if True in x:
    print(0)
    exit()

def fib(count, nums: t.List[int]):
    if len(nums) == n:
        return nums
    n_list = [i for i in nums[-4:] if not is_even(i)]
    nums.append(sum(n_list))
    return fib(count, nums)


print(fib(n, n_nums))
