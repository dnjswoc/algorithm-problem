import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappush, heappop

'''
문제를 보고 최소힙을 만들겠다는 생각을 먼저 했습니다.
하지만 최소힙을 만들 때 루트 노드에 절댓값이 가장 작고,
절댓값이 같으면 작은 값이 오도록 설계하면 되겠다고 생각했습니다.
그리고 heapq로는 할 수 없을 것 같아 직접 삽입, 삭제 함수를 만들면서
우선순위(절댓값이 작고, 절댓값이 같으면 작은 값이 우선순위 높음)가 높은 수를 1번 인덱스에 오도록 코드를 짰습니다.
예
N = 18
list = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]
output
-1 1 0 -1 -1 1 1 -2 2 0
'''

def enq(n):     # 힙 삽입 함수
    global last
    last += 1   # 힙의 마지막 자리 인덱스 + 1
    h[last] = n  # 그 자리에 n 삽입
    c = last    # 자식 노드 인덱스
    p = c // 2  # 부모 노드 인덱스
    while p >= 1 and abs(h[p]) >= abs(h[c]):    # 부모 노드가 없거나 부모 노드의 절댓값이 자식 노드보다 작아질 때까지 반복
        if abs(h[p]) == abs(h[c]) and h[p] < h[c]:  # 절댓값이 같고, 부모 노드 값이 더 작은 경우는 건너뛰기
            continue        # ex. h[p] = -2, h[c] = 2이면 순서가 바뀌면 안된다.
        h[p], h[c] = h[c], h[p] # 그렇지 않은 경우는 순서를 바꿔준다.(우선순위가 높은 것을 앞쪽 인덱스로 보낸다)
        c = p
        p = c // 2


def deq():  # 힙 삭제 함수
    global last
    tmp = h[1]  # 빼낼 1번 인덱스 값을 tmp에 저장
    h[1] = h[last]  # 1번 인덱스 값을 last 인덱스 값으로 복사
    last -= 1
    p = 1   # 부모 노드
    c = p * 2   # 자식 노드
    while c <= last:    # 자식 노드가 last를 넘지 않을 때까지 반복
        # 자식 노드들의 우선순위를 비교하여 c+ 1이 더 높은 우선순위라면 c + 1로 변경
        if c + 1 <= last and abs(h[c]) >= abs(h[c + 1]):
            if abs(h[c]) == abs(h[c + 1]) and h[c] < h[c + 1]:
                c = c
            else:
                c += 1
        if abs(h[p]) >= abs(h[c]):  # 자식 노드와 부모 노드를 비교하여 자식 노드의 우선순위가 더 높으면 자리 변경
            if abs(h[p]) == abs(h[c]) and h[p] < h[c]:
                continue
            h[p], h[c] = h[c], h[p]
            p = c
            c = p * 2
        else:
            break
    return tmp


N = int(input())
arr = [int(input()) for _ in range(N)]
# print(arr)
h = [0] * (N + 1)
last = 0
for num in arr:     # 입력 받은 리스트를 순회하며
    if num:     # 숫자가 0이 아니라면 enq
        enq(num)
        continue
    if last == 0:   # 숫자가 0이고 last가 0이라면
        print(0)    # 0 출력
    else:           # 숫자가 0이고 last가 0이 아니라면 deq
        print(deq())

# N = int(input())
# arr = [int(input()) for _ in range(N)]
#
# heap = []
#
# for num in arr:
#     if num:
#         heappush(heap, num)
#         continue
#     if not heap:
#         print(0)
#         continue
#     print(heappop(heap))
