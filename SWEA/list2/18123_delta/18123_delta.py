T = int(input())                        # 테스트 케이스 입력

di = [0, 1, 0, -1]                      # 델타 탐색(행)
dj = [1, 0, -1, 0]                      # 델타 탐색(열)

for test_case in range(T):              # 테스트 케이스만큼 반복
    N = int(input())                    # 행, 열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 행렬 입력
    abs_sum = 0                         # 차의 절댓값 합을 구할 변수 생성
    for row in range(N):                # 행 반복
        for col in range(N):            # 열 반복
            for delta in range(4):      # 델타 탐색
                n_row = row + di[delta]
                n_col = col + dj[delta]
                if 0 <= n_row < N and 0 <= n_col < N:   # 유효한 인덱스 추출
                    sum_num = arr[row][col] - arr[n_row][n_col]  # 상, 하, 좌, 우 뺄셈 
                    if sum_num < 0:     # 차의 값이 음수이면
                        abs_sum += -sum_num     # 음수 부호 붙여서 계산
                    else:
                        abs_sum += sum_num
    print(f'#{test_case+1} {abs_sum}')  # output 출력



