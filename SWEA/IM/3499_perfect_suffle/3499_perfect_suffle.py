'''
카드 개수의 절반을 기준으로 0부터 시작하는 덩어리, 절반부터 시작하는 덩어리를 나누어
두 덩어리에서 하나씩 꺼내어 한 리스트에 넣으면 되겠다고 생각하고 문제에 접근했습니다.
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    card_arr = list(input().split())
    suffle_card = []
    num = N // 2        # 짝수 일 때
    if N % 2:           # 홀수 일 때
        num = (N // 2) + 1
    i = 0
    while len(suffle_card) < N:
        suffle_card.append(card_arr[i])  # 첫 번째 값부터 리스트에 저장
        if len(suffle_card) == N:   # 입력 값 개수와 같아지면 반복문 탈출
            break
        suffle_card.append(card_arr[i + num])   # 입력 값 절반 이후의 인덱스부터 리스트에 저장
        i += 1
    print(f'#{test_case + 1}', end=' ')
    print(*suffle_card)
