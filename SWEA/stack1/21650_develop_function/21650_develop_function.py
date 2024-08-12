import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    progress_list = list(map(int, input().split()))
    speeds = list(map(int, input().split()))
    days = []
    func_count = 0
    for i in progress_list:
        func_count += 1
    for j in range(func_count):
        progress_day = (100 - progress_list[j]) / speeds[j]
        if (100 - progress_list[j]) % speeds[j] != 0:
            progress_day = ((100 - progress_list[j]) // speeds[j]) + 1
        days += [int(progress_day)]
    print(days)
