# 22:40 - 23:30
# 12:36 - 14:10
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
# 델타 탐색
dij = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]


def play_othello():     # 오셀로 게임 진행
    for turn in play_turn:
        empty_plate[turn[1] - 1][turn[0] - 1] = turn[2]
        for di, dj in dij:
            ni = turn[1] - 1 + di
            nj = turn[0] - 1 + dj
            flip_list = []
            while 0 <= ni < N and 0 <= nj < N and empty_plate[ni][nj] != 0 and empty_plate[ni][nj] != turn[2]:
                flip_list.append([ni, nj])
                ni += di
                nj += dj
            if 0 <= ni < N and 0 <= nj < N and empty_plate[ni][nj] == turn[2]:
                for flip_i, flip_j in flip_list:
                    empty_plate[flip_i][flip_j] = turn[2]


def count_plate():  # 흑돌 백돌 개수 계산
    count_black = 0
    count_white = 0
    for row in range(N):
        for col in range(N):
            if empty_plate[row][col] == 1:
                count_black += 1
                continue
            if empty_plate[row][col] == 2:
                count_white += 1
    return count_black, count_white


for test_case in range(T):
    N, M = map(int, input().split())
    play_turn = [list(map(int, input().split())) for _ in range(M)]
    empty_plate = [[0] * N for _ in range(N)]   # 빈 판
    for i in range(N // 2 - 1, N // 2 + 1):     # 빈 판의 가운데 백돌, 흑돌 번갈아 가며 2개씩 배치
        for j in range(N // 2 - 1, N // 2 + 1):
            if i == j:
                empty_plate[i][j] = 2
                continue
            empty_plate[i][j] = 1
    play_othello()
    for row in range(N):
        for col in range(N):
            print(empty_plate[row][col], end=' ')
        print()
    black, white = count_plate()
    print(f'#{test_case+1} {black} {white}')
