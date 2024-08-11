import sys
sys.stdin = open('input.txt', 'r')

T = int(input())                # 테스트 케이스

for test_case in range(T):
    N = int(input())            # 정방행렬의 크기
    farm_arr = [list(map(int, input())) for _ in range(N)]  # 행렬 입력
    farm_sum = 0                # 농작물 수익
    center_col = N//2           # 기준이 되는 값
    for row in range(N):        # 행 반복
        if row <= center_col:   # 행이 기준 값보다 작거나 같으면
            for col in range(center_col - row, center_col + row + 1):   # 하나씩 커지면서 덧셈
                farm_sum += farm_arr[row][col]
            continue
        for col in range(center_col - (N - row - 1), center_col + (N - row)): # 기준 값 넘어서면
            farm_sum += farm_arr[row][col]  # 하나씩 감소하며 덧셈
    print(f'#{test_case+1} {farm_sum}')
