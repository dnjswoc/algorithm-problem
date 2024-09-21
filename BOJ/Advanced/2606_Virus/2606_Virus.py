import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

'''
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면
그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가
웜 바이러스에 걸리면 웜 바이러스는 2번과 5번을 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6
네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워스 사엥서
연결되어 있지 않기 때문에 영향을 받지 않는다.
    1 - 2 - 3       4
     \              |
       5 - 6        7
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가
주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.


이 문제를 보고 저는 1번 컴퓨터에서 웜 바이러스가 퍼지기 때문에 1번 컴퓨터를 시작으로 완전탐색을 하면
웜 바이러스에 걸리게 되는 컴퓨터의 수를 구할 수 있다고 생각하고 DFS, BFS 등의 완전탐색을 통해 문제에 접근했습니다.
'''


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
