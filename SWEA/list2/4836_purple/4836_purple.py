import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    color_arr = [list(map(int, input().split())) for _ in range(N)]
    empty_arr = [[0] * 10 for _ in range(10)]
    for color in color_arr:         # 입력받은 좌표를 따라 사각형의 색을 칠해준다.
        for i in range(color[0], color[2] + 1):  # 입력받은 좌표의 x값
            for j in range(color[1], color[3] + 1):  # 입력받은 좌표의 y값
                empty_arr[i][j] += color[-1]    # 입력받은 색깔 칠해주기
    purple = 0
    for row in range(10):
        for col in range(10):
            if empty_arr[row][col] == 3:    # 색깔이 3이 되면 count
                purple += 1
    print(f'#{test_case + 1} {purple}')
