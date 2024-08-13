import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    num_arr = list(map(int, input().split()))
    for _ in range(M):
        num_arr.append(num_arr.pop(0))      # 리스트 맨 첫번째 인덱스 값을 뽑아서 리스트 맨 뒤에 저장
    print(f'#{test_case+1} {num_arr[0]}')
