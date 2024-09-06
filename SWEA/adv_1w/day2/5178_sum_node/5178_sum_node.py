import sys
sys.stdin = open('input.txt', 'r')

'''
리프 노드의 값들이 주어지고, 노드의 개수도 주어지므로
완전 이진 트리를 먼저 1차원 배열로 나타내고 리프 노드의 값을 완전 이진 트리에 입력하고,
마지막 노드부터 루트 노드 전까지 반복을 하며,
노드들의 부모 노드에 자식 노드의 값을 더해주면 답을 구할 수 있다고 생각하고 문제에 접근했습니다.
'''

T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    leaf_node = [list(map(int, input().split())) for _ in range(M)]

    tree = [0] * (N + 1)    # 완전 이진 트리를 1차원 배열로 나타내기 위한 리스트

    for node in leaf_node:  # 리프 노드들을 순회하며
        tree[node[0]] = node[1]     # 완전 이진 트리 1차원 배열에 값 저장

    for i in range(N, 1, -1):   # 마지막 노드부터 2번 노드까지 반복
        tree[i // 2] += tree[i]  # 부모 노드에 자식 노드의 값을 더해줌
    print(f'#{test_case} {tree[L]}')
