import sys
sys.stdin = open('input.txt', 'r')


def in_order(node):
    if not node:    # 하위 노드가 없으면 return
        return
    in_order(node_arr[node - 1][2])     # 왼쪽 자식으로 재귀
    answer.append(node_arr[node - 1][1])    # 중위순회 순서를 리스트에 저장
    in_order(node_arr[node - 1][3])     # 오른쪽 자식으로 재귀


for test_case in range(10):
    N = int(input())
    node_arr = [list(input().split()) for _ in range(N)]
    answer = []  # 중위순회 순서를 저장할 리스트

    for arr in node_arr:    # 노드 정보를 하나씩 반복
        i = 0
        while i < len(arr):  # 노드 정보 리스트의 길이보다 작을 때까지 반복
            if i == 1:  # 두번째 자리는 문자열이므로 반복 건너뛰기
                i += 1
                continue
            arr[i] = int(arr[i])    # 나머지 자리는 정수형으로 변환
            i += 1
        while len(arr) < 4:  # 리스트 길이가 4가 될 때까지 0 추가
            arr.append(0)

    in_order(node_arr[0][0])    # 1번 노드부터 중위순회 시작
    print(f'#{test_case + 1}', end=' ')
    print(''.join(answer))
