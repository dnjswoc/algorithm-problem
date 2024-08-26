from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

'''
노드의 거리를 구하는 문제
시작 노드부터 출발하여 BFS를 이용하여 한 단계씩 탐색하므로 이 점을 이용하여
다음 단계로 갈 때마다 거리가 하나씩 늘어난다고 생각했습니다.
그래서 방문표시를 할 visited 리스트를 하나 만들고,
다음 단계로 넘어갈 때마다 거리를 기록할 distance 리스트를 하나 만들었습니다. 
'''

T = int(input())


def bfs(s, g, visited, distance):  # BFS를 통해 최단 거리 구하기
    queue = deque([s])  # 큐 생성
    visited[s] = 1  # 시작 지점 방문 표시
    while queue:    # 큐가 공백상태일 때까지 반복
        v = queue.popleft()
        for i in adjL[v]:
            if not visited[i]:  # v의 인접 노드 i에 방문한 적이 없으면
                queue.append(i) # i를 큐에 삽입
                visited[i] = 1  # 방문 표시
                distance[i] = distance[v] + 1   # 이전 단계(v)까지 걸린 거리 +1
                if i == g:      # i가 g에 도달하면 탈출
                    break
    if not visited[g]:  # 큐가 공백상태인데도 g에 방문한 적이 없으면
        distance[g] = 0  # 0으로 표시


for test_case in range(T):
    V, E = map(int, input().split())
    E_list = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)     # 방문 표시를 남기기 위한 리스트
    distance = [0] * (V + 1)    # 거리를 기록하기 위한 리스트
    for v1, v2 in E_list:   # 인접리스트 만들기 ex. [[], [4, 3], [3, 5] ... ]
        adjL[v1].append(v2)
        adjL[v2].append(v1)     # 양방향이므로 반대 상황(v2 -> v1)도 작성
    bfs(S, G, visited, distance)    # S에서 시작해 G로 갈 수 있는지 BFS 탐색
    print(f'#{test_case + 1} {distance[G]}')
