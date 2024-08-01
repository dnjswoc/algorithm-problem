T = 10

for test_case in range(T):
    N = int(input())
    ladder_arr = [list(map(int, input().split())) for _ in range(10)]
    start_index = 0
    for i in range(10):
        if ladder_arr[-1][i] == 2:
            start_index = i
    print(start_index)
    for row in range(9, -1, -1):
        for col in range(1, 3):
            ladder_arr[row][start_index]
            # if
    # print(f'#{test_case+1} {answer}')