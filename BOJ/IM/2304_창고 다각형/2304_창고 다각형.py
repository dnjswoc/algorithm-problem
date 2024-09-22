import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
col_arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 1, 0, -1):   # 입력 받은 2차원 배열을 x좌표 순으로 정렬
    for j in range(i):
        if col_arr[j][0] > col_arr[j + 1][0]:
            col_arr[j], col_arr[j + 1] = col_arr[j + 1], col_arr[j]

height_arr = [0] * N
for k in range(N):  # 빈 배열에 기둥 높이 입력
    height_arr[k] = col_arr[k][1]
for p in range(N - 1):  # 최대 높이의 기둥을 구하기 위한 반복문
    if height_arr[p] > height_arr[p + 1]:
        height_arr[p], height_arr[p + 1] = height_arr[p + 1], height_arr[p]
max_height = height_arr[-1]  # 마지막 인덱스가 가장 높은 기둥의 높이가 된다.

warehouse_area = 0
for num in [0, -1]:  # 맨 왼쪽의 기둥과 맨 오른쪽 기둥에서 시작하여
    height = 0
    while True:
        if height < col_arr[num][1]:    # 높이가 커질 때마다
            height = col_arr[num][1]    # 높이를 변경하여
        if height == max_height:    # 최대 높이가 되면 반복문 탈출
            break
        if num >= 0:    # 왼쪽 기둥에서 출발할 때의 창고 넓이
            warehouse_area += (height * abs(col_arr[num][0] - col_arr[num + 1][0]))
            num += 1
            continue
        warehouse_area += (height * abs(col_arr[num][0] - col_arr[num - 1][0]))  # 맨 오른쪽 기둥에서 출발할 때
        num -= 1
# 가장 높은 기둥 높이에서의 창고 넓이를 구하지 않았고, 가장 높은 기둥의 높이가 2개 이상일수도 있으므로
max_col_arr = []
for col in col_arr:
    if max_height == col[1]:    # 가장 높은 기둥 높이가 나오면
        max_col_arr.append(col[0])  # 리스트에 저장(이미 정렬되어 있는 채로 순회하여 정렬할 필요는 없음)

if len(max_col_arr) > 1:    # 가장 높은 기동이 2개 이상일 경우
    warehouse_area += (max_col_arr[-1] - max_col_arr[0] + 1) * max_height   # 넓이를 구해서 창고 넓이에 더해줌
else:   # 1개일 경우
    warehouse_area += max_height    # 기둥 높이만 더해준다.
print(warehouse_area)
