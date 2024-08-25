# 19:20 - 20:00
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(s, g, visited):     # DFS 함수
    global answer   # global 선언
    visited[s] = 1  # 시작하는 곳을 방문 표시
    for num in adj_L[s]:    # s에서 인접하는 곳을 반복
        if num == g:    # 인접하는 곳에 도착점이 있으면
            answer = 1  # answer를 1로 변경 후 return
            return
        if visited[num] == 0:   # 인접하는 곳에 도착점이 없고, 방문하지 않은 곳이 있으면
            dfs(num, g, visited)    # DFS 재귀


for test_case in range(T):
    V, E = map(int, input().split())    # V : 노드 개수, E : 간선 개수
    E_list = [list(map(int, input().split())) for _ in range(E)]    # 간선 정보
    S, G = map(int, input().split())    # S : 출발 노드, G : 도착 노드
    visited = [0] * (V + 1)
    adj_L = [[] for _ in range(V + 1)]  # 인접리스트
    answer = 0
    for v1, v2 in E_list:   # 인접리스트 만들기
        adj_L[v1].append(v2)    # v1에서 출발하여 v2로 도착하도록 표시
    dfs(S, G, visited)
    print(f'#{test_case + 1} {answer}')

