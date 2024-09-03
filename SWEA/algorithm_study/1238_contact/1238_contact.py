# 00:00 - 01:20
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

'''
연락이 가는 데 가장 시간이 오래 걸린 노드를 구하는 문제라서 BFS를 쓰면 되겠다고 생각했습니다.
노드의 거리 문제처럼 BFS로 걸리는 시간을 구해서 가장 오래 걸리는 시간의 노드를 구하면 되겠다고 생각했습니다.
첫 번째 테스트 케이스로 예를 들면,
입력 값
24 2
100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2

인접리스트 : adjL = [[], [], [7, 15], [], [10, 2], ... , [17, 8, 7]]
걸린 시간 : times = [0, 0, 0, 0, 2, 0, 0, 1, 3, ... , 0, 0, 2]
이 예시에서 max(times) = 3(8, 10, 17)이고, 이 중 번호가 가장 큰 사람을 구하는 것이므로
max(times) = 3인 가장 큰 인덱스 번호를 구하면 되겠다고 생각하고 문제를 풀었습니다.  
'''

T = 10


def contact(num):       # bfs로 연락을 돌리는 함수
    queue = deque()
    queue.append(num)   # 시작 노드를 큐에 추가
    visited[num] = 1    # 시작 노드 방문 표시
    while queue:    # 큐가 빌 때까지 반복
        v = queue.popleft()
        for i in adjL[v]:   # v의 인접 노드인 i들을 반복  ex) v = 2, i = 7, 15
            if visited[i]:  # i에 방문한 적 있으면 continue
                continue
            queue.append(i)  # 방문한 적 없으면 큐에 i 추가
            visited[i] = 1  # i 방문 표시
            # v까지 걸린 시간 +1 하여 i의 시간을 dist 리스트에 기록   ex) dist[7] = 0 + 1, dist[15] = 0 + 1
            times[i] = times[v] + 1


for test_case in range(1, T + 1):
    L, S = map(int, input().split())    # L : 입력 받을 숫자 개수, S : 시작 지점
    contact_arr = list(map(int, input().split()))   # 간선 정보(양방향 X)
    N = max(contact_arr)    # 입력 받은 수 중 가장 큰 수(인접리스트, 방문 리스트 등을 만들기 위해 가장 큰 노드가 필요)
    adjL = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)  # 방문 표시를 할 리스트
    times = [0] * (N + 1)    # 걸린 시간을 기록할 리스트
    latest = 0  # 가장 오래 걸린 인덱스 번호

    for i in range(L // 2):  # 간선 정보(출발점, 도착점)이 한번에 나와 있어서 분리하기 위해 L을 반으로 나눠준다
        # 홀수 인덱스는 출발점, 짝수 인덱스는 도착점으로 설정
        v1, v2 = contact_arr[i * 2], contact_arr[i * 2 + 1]
        if v2 not in adjL[v1]:  # 간선 정보를 기록한 적이 없으면
            adjL[v1].append(v2)  # 인접리스트에 기록 ex) adjL = [[], [], [7, 15], [], ... , [7, 8, 17]]
    # print(adjL)
    contact(S)  # 입력 받은 시적 지점을 함수에 넘겨준다
    # print(times)
    for i in range(N + 1):
        # 가장 많이 걸린 시간의 인덱스를 구하는데 같은 값이 있으면 가장 큰 인덱스가 나오면 되므로 break를 걸지 않는다.
        if times[i] == max(times):
            latest = i

    print(f'#{test_case} {latest}')
