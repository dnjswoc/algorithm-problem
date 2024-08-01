T = int(input())


def matrix_arr(empty_arr, num_arr, arr_len):
    for i in range(arr_len):
        for j in range(arr_len):
            empty_arr[i][j] = num_arr[j+i*arr_len]
    return empty_arr


def snail_arr():
    pass


for test_case in range(T):
    N = int(input())
    arr = list(range(1, (N**2)+1))
    empty_matrix_arr = [[0] * N for _ in range(N)]
    new_arr = matrix_arr(empty_matrix_arr, arr, N)
    print(new_arr)
    for i in range(N):
        new_arr[i][N-1] = N+i
    for i in range(N-1, -1, -1):
        new_arr[N-1][i] = 10 -i
    print(new_arr)
    # print(list(range(N-1, -1, -1)))
    # print(f'#{test_case+1}')
    # print()
