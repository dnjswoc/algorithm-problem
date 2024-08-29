# 11:35 - 12:27
'''
진기가 붕어빵을 만들어내는 시간이 지나고 손님이 도착해야 하고,
만들어낸 붕어빵 개수보다 손님의 수가 적어야 한다고 생각하고 문제에 접근했습니다.
그리고 손님이 도착하는 시간이 시간 순으로 입력되지 않아서 손님이 도착하는 시간을 정렬했습니다.
'''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def customer_sort(arr):            # 도착하는 손님들의 시간을 버블정렬
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def check_sale():       # 붕어빵을 제 시간에 줄 수 있는지 확인하는 함수
    i = 1
    while True:
        K_i = K * i
        if K_i >= N:    # (한 턴마다 나오는 붕어빵 수 * 턴 수)가 손님의 수보다 크면
            K_i = N     # 손님의 수로 변경
        for num in range(K * (i - 1), K_i):
            if sorted_customer[num] < M * i:   # 한 턴마다 오는 손님의 시간이 붕어빵이 나오는 시간보다 짧으면
                return 'Impossible'     # 손님이 도착하는 제 시간에 줄 수 없음
        i += 1
        if K * (i - 1) >= N:    # (한 턴마다 나오는 붕어빵 수 * 턴 수 - 1)을 넘겨 버리면
            return 'Possible'   # 모든 손님이 제 시간에 받았다는 뜻이 된다.


for test_case in range(T):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    sorted_customer = customer_sort(customer)
    answer = check_sale()
    print(f'#{test_case+1} {answer}')
