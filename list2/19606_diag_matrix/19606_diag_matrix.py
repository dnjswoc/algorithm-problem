T = int(input())

for i in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    sum_diag = 0
    for j in range(N):
        sum_diag = sum_diag + arr[j][j] + arr[N-1-j][j]
    sum_diag -= arr[2][2]
    print(f'#{i+1} {sum_diag}')
