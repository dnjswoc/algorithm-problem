import sys
sys.stdin = open('input.txt', 'r')

num_arr = [list(map(int, input().split())) for _ in range(4)]   # 4줄 입력
empty_arr = [[0] * 100 for _ in range(100)]  # 빈 좌표
rectangle_sum = 0   # 전체 사각형 합
for num in num_arr:
    for row in range(num[0], num[2]):   # x좌표
        for col in range(num[1], num[3]):   # y좌표
            empty_arr[row][col] += 1    # 사각형에 해당하는 좌표에 +1
for i in range(100):
    for j in range(100):
        if empty_arr[i][j] > 0:  # 빈 좌표에 추가된 값이 1 이상이면 
            rectangle_sum += 1  # 사각형 넓이에 포함
print(rectangle_sum)
