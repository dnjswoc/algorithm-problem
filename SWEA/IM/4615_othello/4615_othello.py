# 22:40 - 23:30
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
# 델타 탐색
dij = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]


def play_othello():     # 오셀로 게임 진행
    for turn in play_turn:
        empty_plate[turn[1] - 1][turn[0] - 1] = turn[2]
        for di, dj in dij:
            for r in range(N - 1, 0, -1):   # 8 방향을 행렬 길이만큼 탐색
                ni = turn[1] - 1 + (di * r)
                nj = turn[0] - 1 + (dj * r)
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                if empty_plate[ni][nj] == turn[2]:  # 입력한 돌과 같은 돌이 나오면
                    for k in range(1, r):     # 그 사이의 돌을 모두 같은 종류로 변경
                        empty_plate[turn[1] - 1 + (di * k)][turn[0] - 1 + (dj * k)] = turn[2]


def count_plate():  # 흑돌 백돌 개수 계산
    count_black = 0
    count_white = 0
    for row in range(N):
        for col in range(N):
            if empty_plate[row][col] == 1:
                count_black += 1
                continue
            count_white += 1
    return count_black, count_white


for test_case in range(T):
    N, M = map(int, input().split())
    play_turn = [list(map(int, input().split())) for _ in range(M)]
    empty_plate = [[0] * N for _ in range(N)]   # 빈 판
    for i in range(N // 2 - 1, N // 2 + 1):     # 빈 판의 가운데 백돌, 흑돌 각 2개씩 배치
        for j in range(N // 2 - 1, N // 2 + 1):
            if i == j:
                empty_plate[i][j] = 2
                continue
            empty_plate[i][j] = 1
    play_othello()
    black, white = count_plate()
    print(f'#{test_case+1} {black} {white}')
