'''
1번에서 가장 먼 노드의 개수를 구하는 문제이므로
BFS로 1번부터 각 노드까지의 거리를 구한 후 가장 먼 거리에
해당하는 노드의 개수를 구하였습니다.
'''


from collections import deque


def solution(n, edge):
    # BFS로 1번 노드에서 각 노드까지의 거리를 구한다.
    def bfs(start):
        queue = deque([start])
        # 시작 노드 방문 표시
        visited[start] = 1

        # queue가 빌 때까지 반복
        while queue:
            start = queue.popleft()

            # 인접 노드들을 비교하여 방문
            for v in adjL[start]:
                # 방문한 적 있는 노드면 continue
                if visited[v]:
                    continue
                queue.append(v)
                # 해당 노드까지의 거리는 그 전까지 노드의 거리 +1을 해준다.
                visited[v] = visited[start] + 1

    visited = [0] * (n + 1)
    adjL = [[] for _ in range(n + 1)]

    # 인접리스트 만들기(양방향으로 만들어준다.)
    for lst in edge:
        adjL[lst[0]].append(lst[1])
        adjL[lst[1]].append(lst[0])

    # print(adjL)

    bfs(1)
    answer = 0
    
    # 가장 먼 거리에 해당하는 노드의 개수를 구한다.
    for i in range(n + 1):
        if visited[i] == max(visited):
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))