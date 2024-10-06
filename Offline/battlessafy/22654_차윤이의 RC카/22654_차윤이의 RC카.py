import sys
sys.stdin = open('input.txt')

# 강사님 코드
# # RC카는 항상 위를 바라보고 시작한다.
# # R이 입력되면 오른쪽으로 90도 회전한다.   -> 바라보는 방향 index가 1 증가한다.
# # L이 입력되면 왼쪽으로 90도 회전한다.     -> 바라보는 방향 index가 1 감소한다.
# #      상 우 하 좌
# #      0  1  2  3
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# def search(my_position, command_list):
#     x, y = my_position                      # 내 위치 x, y 초기화
#     command_len, command = command_list     # 총 커맨드 길이와 커맨드 초기화
#     # 처음 바라보는 방향은 위. (0번 index)
#     dir = 0
#     for i in range(command_len):    # 총 입력 길이 만큼 진행
#         if command[i] == 'A':       # 이동 명령이라면,
#             nx = x + dx[dir]          # 해당 위치로 이동하였을 때의 좌표 작성
#             ny = y + dy[dir]
#             # 범위를 벗어나지 않거나, 나무가 아닌 경우에만 이동 (범위를 벗어나거나 나무라면 그 자리에서 움직이지 않는다.)
#             # 목적지라고 하더라도 이동 할 수 있음에 유의 (지나치는 경우도 있을 수 있다.)
#             if 0 <= nx < N and 0 <= ny < N and map_data[nx][ny] != 'T':
#                 x, y = nx, ny   # 내 현재 위치를 변경
#         else:                           # 이동 명령이 아닌 경우
#             if command[i] == 'R':       # R이면 오른쪽으로 90도 회전
#                 dir += 1                # 현재 dir이 0 이었다면 1 증가: ex) 0번 index는 위를, 1번 index는 오른쪽을 의미
#             elif command[i] == 'L':     # L이면 왼쪽으로 90도 회전
#                 dir -= 1                # 현재 dir이 2 였다면 1 감소: ex) 2번 index는 아래를, 1번 index는 오른쪽을 의미
#
#             # dir 계산 종료후, 범위가 잘못된 경우에 대해서 처리
#             if dir >= 4:    # 계속 오른쪽으로 회전해서 dir이 4 이상이 된다면,
#                 # 왼쪽을 바라보고 있던 상황 (3) 에서 오른쪽 회전으로 1 증가한 경우, 이때는 위를 바라봐야 하므로 0으로 초기화
#                 dir = 0
#             if dir <= -1:   # 계속 왼쪽으로 회전해서 dir이 -1 이하가 된다면,
#                 # 위를 바라보고 있던 상황 (0) 에서 왼쪽 회전으로 1 감소한 경우, 이때는 왼쪽을 바라봐야 하므로 4로 초기화
#                 dir = 3
#     # 모든 입력이 종료된 이후,
#     if map_data[x][y] == 'Y':   # 도착지점이라면
#         return 1                # 성공
#     else:                       # 아니라면
#         return 0                # 실패
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())    # 맵의 크기 N*N
#     # 입력받은 각 줄의 문자열을 한 단어씩 쪼개어 리스트에 담는다.
#     map_data = [list(input()) for _ in range(N)]
#     Q = int(input())    # 조종 횟수
#     # 입력 값을 공백기준으로 나눈 후, 해당 값이 정수형이라면, 정수로, 아니면 문자열로 리스트에 담는다.
#     command_list = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(Q)]
#
#     result_list = [0] * Q   # 우선 모두 실패한다고 가정하고 초기화
#
#     # RC카 위치 탐색 (몇 번을 조작하든 시작 위치는 변하지 않음)
#     for x in range(N):
#         for y in range(N):
#             if map_data[x][y] == 'X':
#                 my_position = [x, y]   # RC카 시작 위치 초기화
#
#     for i in range(Q):  # 총 조종 횟수 만큼 조사
#         # i 번째 조사 (i번째 커맨드 입력에 목적지 도착 유무 판별 후 반환
#         result_list[i] = search(my_position, command_list[i])
#
#     # 결과 출력
#     print(f'#{tc}', *result_list)


# 내가 푼 코드
T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def search(my_position, command_list):
    x, y = my_position
    command_len, command = command_list

    dir = 0

    for i in range(command_len):
        if command[i] == 'A':
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N and map_data[nx][ny] != 'T':
                x, y = nx, ny

        else:
            if command[i] == 'R':
                dir += 1
            elif command[i] == 'L':
                dir -= 1

            if dir >= 4:
                dir = 0
            if dir <= -1:
                dir = 3

    if map_data[x][y] == 'Y':
        return 1
    else:
        return 0


for tc in range(1, T + 1):
    N = int(input())
    map_data = [list(input()) for _ in range(N)]
    Q = int(input())
    command_list = [list(input().split()) for _ in range(Q)]

    result_list = [0] * Q

    for i in range(Q):
        command_list[i][0] = int(command_list[i][0])

    for x in range(N):
        for y in range(N):
            if map_data[x][y] == 'X':
                my_position = [x, y]

    for i in range(Q):
        result_list[i] = search(my_position, command_list[i])

    print(f'#{tc}', end=' ')
    print(*result_list)
