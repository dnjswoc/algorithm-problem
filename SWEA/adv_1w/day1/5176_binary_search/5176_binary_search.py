import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def tree(num):  # 완전 이진 트리 생성
    if not num:
        return
    tree(left[num])
    in_order.append(num)    # 중위 순회의 순서를 리스트에 저장
    tree(right[num])


for test_case in range(T):
    N = int(input())
    answer_1 = 0
    answer_2 = 0
    in_order = []   # 중위 순회의 순서를 저장할 리스트

    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(2, N + 1):   # i를 2부터 N+1 까지 반복하며 완전 이진 트리를 만들기 위해서는
        # i가 짝수일 때는 left, 홀수일 때는 right에 저장되어야 하므로
        # ex) N=6일 때, left[1] = 2, right[1] = 3이어야 하므로 i//2 몫을 인덱스로 하여 i를 저장
        if i % 2 == 0:  # i가 짝수이면
            left[i // 2] = i
        else:           # i가 홀수이면
            right[i // 2] = i

    tree(1)     # 1을 root node로 하여 트리 만들기

    for i in range(N):
        if in_order[i] == 1:    # 중위 순회 순서에서 1의 값을 갖는 인덱스를 추출
            answer_1 = i + 1
        if in_order[i] == N // 2:   # 중위 순회 순서에서 N//2의 값을 갖는 인덱스를 추출
            answer_2 = i + 1

    print(f'#{test_case + 1} {answer_1} {answer_2}')
