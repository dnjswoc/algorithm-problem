from collections import deque


def bfs(arr, x, y, visited):
    queue = deque([x, y])
    visited[x][y] = 1
    while queue:
        vx = queue.popleft()
        vy = queue.popleft()
        for dx, dy in dxy:
            nx = vx + dx
            ny = vy + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if arr[nx][ny]:
                continue
            queue.append(nx)
            queue.append(ny)
            visited[nx][ny] = 1


dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N ,M = map(int, input().split())
ice_arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ice_cnt = 0
for row in range(N):
    for col in range(M):
        if ice_arr[row][col]:
            continue
        if visited[row][col]:
            continue
        bfs(ice_arr, row, col, visited)
        ice_cnt += 1
print(ice_cnt)
