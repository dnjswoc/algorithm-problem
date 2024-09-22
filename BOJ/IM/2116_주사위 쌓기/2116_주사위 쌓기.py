import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
dice_arr = [list(map(int, input().split())) for _ in range(N)]
dice_dict = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}    # 마주보고 있는 주사위
dice_num = [1, 2, 3, 4, 5, 6]   # 주사위 눈의 종류
max_dice_sum = 0    # 최대로 나올 수 있는 주사위 옆면의 합

for i in range(6):  # 하나의 주사위의 모든 값을 순회
    row = 0
    col = i
    side_num = []   # 옆면에 존재하는 주사위 눈
    dice_sum = 0    # 옆면에 존재하는 주사위 눈의 최대 합
    while row < N:  # 행을 더하며 반복
        bot_num = dice_arr[row][col]    # 바닥에 위치할 주사위 눈
        top_num = dice_arr[row][dice_dict[col]]  # 위에 위치할 주사위 눈(바닥 주사위 눈과 맞은 편 -> 딕셔너리로 구함)
        for num in dice_num:    # 바닥과 위에 위치할 주사위 눈을 제외한 주사위 눈 구하기
            if num != bot_num and num != top_num:
                side_num.append(num)    # 리스트가 오름차순으로 정렬된 채로 반복하였으므로 마지막 인덱스가 최댓값이 된다.
        dice_sum += side_num[-1]    # 그 값들을 더해준다.
        row += 1
        for j in range(6):
            if row < N and dice_arr[row][j] == top_num:  # 그 전 행에서 위에 위치한 값이 바닥에 오게 되고, 그 인덱스를 찾는 과정
                col = j
                break
    if max_dice_sum < dice_sum:
        max_dice_sum = dice_sum
print(max_dice_sum)

