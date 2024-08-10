import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    farm_arr = [list(map(int, input())) for _ in range(N)]
    farm_sum = 0
    center_col = N//2
    for row in range(N):
        if row <= center_col:
            for col in range(center_col - row, center_col + row + 1):
                farm_sum += farm_arr[row][col]
            continue
        for col in range(center_col - (N - row)//2, center_col + (N - row)//2 + 1):
            farm_sum += farm_arr[row][col]
    print(f'#{test_case+1} {farm_sum}')
