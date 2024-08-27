import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def subtree(num, lst):  # 서브트리의 노드 개수를 구하는 함수(num : 출발하는 지점, lst : 서브트리에 존재하는 노드를 저장하는 리스트)
    if not num:     # 시작하는 값이 0이라면 return
        return
    lst.append(num) # 시작하는 값이 0이 아니라면 subtree_lst에 저장하고
    subtree(left[num], lst)     # 해당 노드의 왼쪽 자식을 재귀
    subtree(right[num], lst)    # 해당 노드의 오른쪽 자식을 재귀


for test_case in range(T):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    subtree_lst = []    # 서브트리에 존재하는 노드의 번호를 저장하는 리스트

    par = [0] * (E + 2)     # 부모
    left = [0] * (E + 2)    # 왼쪽 자식
    right = [0] * (E + 2)   # 오른쪽 자식

    for i in range(len(arr) // 2):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if not left[p]:     # p 노드의 왼쪽 자식이 비어있는 상태면
            left[p] = c     # left의 p 인덱스에 저장
        else:               # p 노드의 오른쪽 자식이 비어있는 상태면
            right[p] = c    # right의 p 인덱스에 저장
        par[c] = p          # par의 c(자식 노드 번호) 인덱스에 p(부모 노드 번호) 저장

    subtree(N, subtree_lst)     # N에서 출발하는 서브트리 노드의 개수를 구함
    print(f'#{test_case + 1} {len(subtree_lst)}')

