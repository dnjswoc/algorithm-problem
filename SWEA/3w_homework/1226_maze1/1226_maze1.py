import sys
sys.stdin = open('input.txt', 'r')


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

