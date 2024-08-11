import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    num_arr = list(input().split())
    for i in range(len(num_arr)):
        if i % 2 == 0:
            num_arr[i] = int(num_arr[i])
    print(num_arr)
