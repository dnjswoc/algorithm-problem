T = int(input())


def binary_tree(num):
    if num > N:
        return
    binary_tree(num * 2)
    binary_tree(num * 2 + 1)


for test_case in range(1, T + 1):
    N = int(input())
    node_arr = list(map(int, input().split()))

