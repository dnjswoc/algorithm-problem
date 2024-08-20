T = int(input())

for test_case in range(T):
    N = int(input())
    light_arr = list(map(int, input().split()))
    start_arr = [0] * N
    switch_cnt = 0
    while start_arr != light_arr:
        for i in range(N):
            if start_arr[i] != light_arr[i]:
                idx = i
                break
        times = N // (idx + 1)
        for time in range(1, times + 1):
            if start_arr[((idx + 1) * time) - 1]:
                start_arr[((idx + 1) * time) - 1] = 0
            else:
                start_arr[((idx + 1) * time) - 1] = 1
        switch_cnt += 1
    print(f'#{test_case + 1} {switch_cnt}')
