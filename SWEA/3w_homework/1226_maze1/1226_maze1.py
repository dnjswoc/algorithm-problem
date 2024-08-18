import sys
sys.stdin = open('input.txt', 'r')


def start_idx(arr):
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return i, j


def check_maze(arr, x, y):
    visited = [[0] * 16 for _ in range(16)]
    queue = [x, y]
    while queue:
        x, y = queue.pop(0), queue.pop(0)
        if not visited[x][y]:
            visited[x][y] = True
            for di, dj in dij:
                ni = x + di
                nj = y + dj
                if arr[ni][nj] == 3:
                    return 1
                if arr[ni][nj] == 1:
                    continue
                if not visited[ni][nj]:
                    queue.append(ni)
                    queue.append(nj)
    return 0


dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for test_case in range(10):
    T = int(input())
    maze_arr = [list(map(int, input())) for _ in range(16)]
    start_idx_x, start_idx_y = start_idx(maze_arr)
    print(f'#{T} {check_maze(maze_arr, start_idx_x, start_idx_y)}')

