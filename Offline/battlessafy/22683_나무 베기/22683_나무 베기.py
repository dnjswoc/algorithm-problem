import sys
sys.stdin = open('input.txt')


from collections import deque

# RC카는 항상 위를 바라보고 시작한다.
# R이 입력되면 오른쪽으로 90도 회전한다.   -> 바라보는 방향 index가 1 증가한다.
# L이 입력되면 왼쪽으로 90도 회전한다.     -> 바라보는 방향 index가 1 감소한다.
#      상 우 하 좌
#      0  1  2  3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(my_position, target_position, K):
    # 방문 여부를 저장하는 4차원 배열: [x][y][방향][남은 나무 제거 횟수]
    # 각 좌푯값에 대한 x, y로 2차원
    # 한 위치에서 방향만 전환하여도 조작 횟수가 증가하므로 이에 대한 3차원
    # 해당 위치로 이동시에, 나무를 몇 번 잘랐었는지에 따라 경우가 달라지므로 이에 대한 4차원
    visited = [[[[False] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    q = deque()
    x, y = my_position  # 내 좌표 초기화

    # 시작 상태: (x좌표, y좌표, 방향(위), 조작 횟수, 남은 나무 제거 횟수)
    q.append((x, y, 0, 0, K))
    visited[x][y][0][K] = True

    while q:
        x, y, dir, moves, cnt = q.popleft()

        # 현재 방향으로 이동하는 좌표 갱신
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 해당 위치가 목적지라면
        if [nx, ny] == target_position:
            return moves + 1    # 한 칸 전진한 이동 거리 반환

        if 0 <= nx < N and 0 <= ny < N:     # 범위를 벗어나지 않고,
            # 해당위치가 길이면서, 아직 이 방향으로는 방문한적 없다면,
            if map_data[nx][ny] == 'G' and not visited[nx][ny][dir][cnt]:
                visited[nx][ny][dir][cnt] = 1               # 방문 표시
                q.append((nx, ny, dir, moves + 1, cnt))     # 이동 거리 1증가 후, 다음 작업 대상 추가

            # 해당 위치가 나무인데, 아직 나무를 자를 수 있는 횟수가 남았으면서,
            # 이 방향으로, 동일한 횟수의 나무를 자른 만큼 가본 적이 없다면,
            elif map_data[nx][ny] == 'T' and cnt > 0 and not visited[nx][ny][dir][cnt - 1]:
                visited[nx][ny][dir][cnt - 1] = 1               # 나무를 한번 자른 경우에 대해서 방문표시
                q.append((nx, ny, dir, moves + 1, cnt - 1))     # 이동 거리 1증가, 나무를 자른 횟수 1 감소

        # 왼쪽으로 회전
        nd = (dir - 1) % 4
        if not visited[x][y][nd][cnt]:
            visited[x][y][nd][cnt] = 1
            q.append((x, y, nd, moves + 1, cnt))

        # 오른쪽으로 회전
        nd = (dir + 1) % 4
        if not visited[x][y][nd][cnt]:
            visited[x][y][nd][cnt] = 1
            q.append((x, y, nd, moves + 1, cnt))

    # 도착할 수 없는 경우
    return -1


T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 필드 크기와 나무를 벨 수 있는 최대 횟수
    map_data = [list(input()) for _ in range(N)]

    # 내 위치와 목적지 위치 탐색
    for x in range(N):
        for y in range(N):
            if map_data[x][y] == 'X':       # 내 위치를 찾으면
                my_position = [x, y]        # RC카 시작 위치 초기화
            elif map_data[x][y] == 'Y':     # 목적지를 찾으면
                target_position = [x, y]    # 목적지 위치 초기화

    result = bfs(my_position, target_position, K)
    print(f'#{tc} {result}')