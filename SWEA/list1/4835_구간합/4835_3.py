import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    current_sum = sum(num_lst[0:M + 1])
    max_sum = current_sum
    min_sum = current_sum

    for i in range(N - M):
        current_sum = current_sum - num_lst[i] + num_lst[i + M]
        if max_sum <= current_sum:
            max_sum = current_sum
        if min_sum >= current_sum:
            min_sum = current_sum

    print(f'#{test_case + 1} {max_sum - min_sum}')
