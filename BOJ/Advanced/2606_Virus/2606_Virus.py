import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


# DFS 방식의 풀이
def dfs(s):
    # 시작지점 방문 표시
    visited[s] = 1

    # 인접한 노드를 순회하며 방문하지 않은 곳을 재귀로 방문
    for v in adjL[s]:
        if visited[v]:
            continue
        dfs(v)


# BFS 방식의 풀이
def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1
    
    # queue가 빌 때까지 탐색
    while queue:
        v = queue.popleft()
        for i in adjL[v]:
            # 방문하지 않은 곳을 탐색
            if visited[i]:
                continue
            queue.append(i)
            visited[i] = 1


N = int(input())    # N : 컴퓨터의 수
E = int(input())    # E : 네트워크 상에서 연결된 컴퓨터 쌍의 수
node_arr = [list(map(int, input().split())) for _ in range(E)]

adjL = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

# 인접리스트 생성
for node in node_arr:
    adjL[node[0]].append(node[1])
    adjL[node[1]].append(node[0])

# 항상 1번 컴퓨터를 통해 바이러스가 퍼지기 때문에 1번 컴퓨터에서 시작
# dfs(1)
bfs(1)

# 1번 컴퓨터는 답에서 제외해야하므로 visited에서 1인 개수에서 1(1번 컴퓨터)을 뺀다
print(sum(visited) - 1)
