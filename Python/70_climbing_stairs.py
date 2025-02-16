# slow
# def climbStairs(n: int) -> int:
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     return climbStairs(n - 1) + climbStairs(n - 2)


def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    a = 1
    b = 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


print(climbStairs(46))
