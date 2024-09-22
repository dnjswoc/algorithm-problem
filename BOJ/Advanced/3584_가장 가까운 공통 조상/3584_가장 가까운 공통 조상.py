import sys
sys.stdin = open('input.txt', 'r')

'''
입력 값으로 간선 정보(부모 노드 - 자식 노드)가 주어졌으므로
주어진 노드들에서 각각 본인 포함하여 점점 거슬러 올라가 만나는 조상 노드들을 리스트에 저장하면서
가장 먼저 일치하는 노드가 가장 가까운 공통된 조상 노드라고 생각하고 문제에 접근했습니다.
ex. 16, 7
16 - [16, 10, 4, 8]
7 - [7, 6, 4, 8]
따라서 이 예시에서는 답이 4가 됩니다.
'''

T = int(input())


def check_ancestor(arr):    # 노드들의 가장 가까운 공통된 조상 노드를 찾는 함수
    # node_anc = [[16, 10, 4, 8], [7, 6, 4, 8]]에서
    # 0번 리스트의 값 하나를 1번 리스트의 값들과 비교하여 가장 먼저 일치하는 노드를 return
    # 16과 [7, 6, 4, 8]을 비교 ... 4와 [7, 6, 4, 8]을 비교 -> 4 return
    for i in arr[0]:
        for j in arr[1]:
            if i == j:
                return i


for test_case in range(T):
    N = int(input())
    edge_arr = [list(map(int, input().split())) for _ in range(N - 1)]  # 간선 정보
    target_node = list(map(int, input().split()))   # 공통된 조상 노드를 찾을 노드들 ex. 16, 7
    node_anc = []   # 노드들의 조상 노드를 기록할 리스트

    for node in target_node:    # 공통된 조상 노드를 찾을 노드를 반복하며 ex. 16, 7
        anc_arr = [node]    # 노드 자기 자신을 포함한 리스트를 만든다 anc_arr = [16]
        while node > 0:     # 조상 노드가 안 나올 때까지 반복
            for arr in edge_arr:    # 간선 정보를 반복하며
                if node == arr[1]:  # 타겟 노드가 자식노드이면 ex. 16 -> [10, 16]
                    node = arr[0]   # node를 타겟 노드의 부모 노드로 재할당 node = 10
                    anc_arr.append(arr[0])  # 리스트에 부모 노드를 저장 ex. anc_arr = [16, 10]
                    break   # 반복문 탈출
            else:   # 반복문을 다 도는 동안 부모 노드가 나오지 않는다면(루트 노드까지 갔다면)
                node = 0    # node를 0으로 만들어 while문이 끝나게 만든다.
        node_anc.append(anc_arr)    # 조상 노드들을 기록한 리스트를 node_anc 리스트에 저장
    # node_anc = [[16, 10, 4, 8], [7, 6, 4, 8]]
    print(check_ancestor(node_anc))  # 가장 먼저 공통된 조상 노드를 출력


# 나영 코드
def dfs(node, root):

    if graph[node] == 0:
        return

    root.append(graph[node])
    dfs(graph[node], root)

T = int(input())

for case in range(1, T+1):
    N = int(input())  # 노드의 수
    arr = [list(map(int,input().split())) for _ in range(N-1)]
    a, b = map(int,input().split())  # 부모 노드를 찾아야할 두 노드
    graph = [0]*(N+1)

    a_root = [a]
    b_root = [b]

    for p,c in arr:   # 자식노드를 인덱스로 하여 부모노드 기록 / [0, 8, 10, 16, 8, 8, 4, 6, 0, 5, 4, 10, 16, 1, 1, 6, 10]
        graph[c] = p

    dfs(a,a_root)  # [16, 10, 4, 8]
    dfs(b,b_root) # [7, 6, 4, 8]

    ans = 0
    for root in a_root:
        if root in b_root:
            ans = root
            break

    print(ans)