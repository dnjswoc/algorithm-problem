# 15:50 - 16:12

import sys
sys.stdin = open('input.txt', 'r')

# BFS


def start_idx(arr):     # 미로의 시작점을 찾는 함수
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:  # 2이면 시작점이 된다.
                return i, j


def check_maze(arr, x, y):      # 미로가 성립하는지 확인하는 함수
    visited = [[0] * 16 for _ in range(16)]
    queue = [x, y]  # 시작점을 큐에 입력
    while queue:    # 큐가 공백상태가 될 때까지 반복
        x, y = queue.pop(0), queue.pop(0)
        if not visited[x][y]:
            visited[x][y] = True
            for di, dj in dij:
                ni = x + di
                nj = y + dj
                if arr[ni][nj] == 3:    # 탐색 중 3을 찾으면 미로가 성립
                    return 1
                if arr[ni][nj] == 1:    # 1이면 벽이라 갈 수 없음
                    continue
                if not visited[ni][nj]:  # 1도 3도 아니고, 방문한 적이 없으면 그 방향으로 나아감
                    queue.append(ni)
                    queue.append(nj)
    return 0    # 큐가 공백상태가 되도록 3을 찾지 못하면 미로가 성립하지 않음


dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]    # 델타 탐색(우, 하, 좌, 상)

for test_case in range(10):
    T = int(input())
    maze_arr = [list(map(int, input())) for _ in range(16)]
    start_idx_x, start_idx_y = start_idx(maze_arr)
    print(f'#{T} {check_maze(maze_arr, start_idx_x, start_idx_y)}')



# DFS
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def find_start(arr):    # 미로의 시작점을 찾는 함수
    for row in range(16):
        for col in range(16):
            if arr[row][col] == 2:  # 2차원 배열의 값이 2일 때의 행, 열 값을 return
                return row, col


def check_maze(x, y, visited, arr):     # 미로가 성립하는 지 확인하는 함수
    global answer   # 전역변수로 설정
    visited[x][y] = 1   # 입력받은 값의 위치를 방문 표시
    for dx, dy in dxy:  # 델타 탐색(우, 하, 좌, 상)
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= 16 or ny >= 16:    # 유효하지 않은 인덱스 넘기기
            continue
        if arr[nx][ny] == 3:    # 탐색 중 2차원 배열의 값이 3이 되면 answer를 1로 변경
            answer = 1
            return  # 찾음과 동시에 끝내기(이게 백트래킹인가요...?)
        if arr[nx][ny] == 0 and visited[nx][ny] == 0:   # 델타 탐색 중 미로에서 0이 되고, 방문하지 않았으면
            check_maze(nx, ny, visited, arr)    # 재귀로 진행하던 델타 방향으로 계속 탐색


for test_case in range(10):
    N = int(input())
    maze_arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    answer = 0      # 정답, 미로가 성립하지 않을 때의 값 0으로 설정
    start_idx_x, start_idx_y = find_start(maze_arr)
    check_maze(start_idx_x, start_idx_y, visited, maze_arr)
    print(f'#{N} {answer}')

