from collections import deque

"""
문제보고 노드의 거리나 익숙한 문제들이 생각났습니다.
이 문제 역시 도착점까지의 최소 거리를 알아내야 하므로
DFS보다는 BFS로 답을 구하는 게 좋을 것 같다고 생각하고 접근했습니다.
"""


def shortest_path(row, col, visited, arr, N, M):
    dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]    # 우, 하, 좌, 상

    visited[row][col] = 1   # 시작점 방문 표시

    queue = deque([(row, col)])     # 시작점 큐에 삽입

    while queue:    # 큐가 빌 때까지 반복
        i, j = queue.popleft()  # 행, 열 인덱스 pop
        for di, dj in dij:  # 델타 탐색
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if visited[ni][nj]:  # 방문한 적 있으면 continue
                continue
            if arr[ni][nj]:     # 방문한 적 없고 maps의 값이 1이면
                queue.append((ni, nj))  # 큐에 ni, nj 삽입
                visited[ni][nj] = visited[i][j] + 1     # 거리 1 추가

    return visited[N - 1][M - 1]    # 도착점까지 최소 거리 return


def solution(maps):
    N = len(maps)   # 행 길이
    M = len(maps[0])    # 열 길이
    visited = [[0] * M for _ in range(N)]
    answer = shortest_path(0, 0, visited, maps, N, M)
    if answer == 0:  # 도착점까지 최소 거리가 0이면(도착점에 도달하지 못하면)
        answer = -1  # -1 출력
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
