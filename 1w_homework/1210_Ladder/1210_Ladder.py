T = 10

dj = [-1, 1]

for test_case in range(T):
    N = int(input())
    ladder_arr = [list(map(int, input().split())) for _ in range(10)]
    start_index = 0
    for i in range(10):
        if ladder_arr[-1][i] == 2:
            start_index = i
    print(start_index)
    for row in range(9, -1, -1):
        for col in range(2):
            nj = start_index + dj[col]
            if 0 <= nj < 10:
                while ladder_arr[row][nj] != 0:
                    start_index += dj[col]
                    nj = start_index
                    print(start_index)
                ladder_arr[row][start_index] += 1
    for a in range(10):
        print(ladder_arr[a])
    # for j in range(10):
    #     if ladder_arr[0][j] == 2:
    #         print(j)
            # if
    # print(f'#{test_case+1} {answer}')