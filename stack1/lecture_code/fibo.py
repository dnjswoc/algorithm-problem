# # memoization
# def fibo1(n):
#     if n >= 2 and memo[n] == 0:
#         memo[n] = fibo1(n-1) + fibo1(n-2)
#     return memo[n]
#
#
# n = 7
# memo = [0] * (n+1)
# memo[0] = 0
# memo[1] = 1
# print(fibo1(n))
#


# DP(Dynamic Programming)
def fino2(n):
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


print(fino2(7))
