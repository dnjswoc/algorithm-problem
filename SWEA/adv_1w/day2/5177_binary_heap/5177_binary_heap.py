import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappush, heappop

'''
이 문제는 입력 받은 숫자대로 이진 힙을 만들고,
마지막 노드의 조상 노드를 차례로 구해서 더해주기만 하면 되겠다고 생각하고 문제에 접근했습니다.
예를 들어, 7, 2, 5, 3, 4, 6이 입력되면
        2
    3       5
  7   4   6
의 형태로 최소 힙을 만들고, 마지막 노드인 6의 조상 노드들의 합을 구해주었습니다.
'''

# heapq 없는 풀이
T = int(input())


def enq(n):     # heapq 쓰지 않고 함수로 힙에 삽입하는 함수
    global last
    last += 1   # 힙의 마지막 인덱스 +1
    h[last] = n  # 힙의 마지막 인덱스에 n 저장
    c = last    # 자식 노드
    p = c // 2  # 부모 노드
    while p >= 1 and h[p] > h[c]:   # 부모 노드가 있고 부모 노드가 자식 노드보다 크면
        h[p], h[c] = h[c], h[p]     # 부모 노드와 자식 노드 값을 변경
        c = p   # 자식 노드 인덱스를 부모 노드 인덱스로 변경
        p = c // 2  # 부모 노드(자식 노드 // 2)


for test_case in range(1, T + 1):
    N = int(input())
    node_arr = list(map(int, input().split()))

    h = [0] * (N + 1)   # 힙을 1차원 배열로 나타내기 위함
    last = 0    # 마지막 인덱스 관리용 변수

    for num in node_arr:
        enq(num)    # 리스트 순서대로 힙에 삽입

    anc_node = []   # 조상 노드를 기록할 리스트
    while last // 2 > 0:    # 부모 노드가 없을 때까지 반복
        anc_node.append(h[last // 2])   # 리스트에 부모 노드를 기록
        last //= 2
    print(f'#{test_case} {sum(anc_node)}')


# heapq 사용한 풀이
T = int(input())

for test_case in range(1, T + 1):
    N = int(int(input()))
    node_arr = list(map(int, input().split()))

    h = []

    for num in node_arr:
        heappush(h, num)

    h = [0] + h

    anc_node = []  # 조상 노드를 기록할 리스트
    p = N
    while p > 0:  # 부모 노드가 없을 때까지 반복
        p //= 2
        anc_node.append(h[p])  # 리스트에 부모 노드를 기록

    # print(anc_node)
    print(f'#{test_case} {sum(anc_node)}')
