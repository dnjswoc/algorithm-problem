import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def solution():
    target = 1
    for i in range(N):
        if not target << i & M:  # 1을 왼쪽으로 비트는 하나씩 밀어서 M과 다른 비트가 나오면 return False
            return False
    return True     # 1을 왼쪽으로 N - 1번 밀어도 M과 비트가 다른 비트가 나오지 않으면 return True


for test_case in range(1 ,T + 1):
    N, M = map(int, input().split())
    result = solution()

    if result:
        print(f'#{test_case} ON')
    else:
        print(f'#{test_case} OFF')
