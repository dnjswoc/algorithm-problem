T = 10                                      # 테스트 케이스

for test_case in range(T):                  # 테스트 케이스만큼 반복
    N = int(input())                        # 테스트 케이스 입력
    arr = [list(map(int, input().split())) for _ in range(100)]  # 100X100 행렬 입력
    M = 100                                 # 행, 열 크기
    row_sum_list = []                       # 행 합계를 저장할 리스트 생성
    col_sum_list = []                       # 열 합계를 저장할 리스트 생성
    diagonal_sum_1 = 0                      # 대각원소의 합을 저장할 변수 생성
    diagonal_sum_2 = 0                      # 대각원소의 합을 저장할 변수 생성
    for row in range(M):                    # 행 반복
        row_sum = 0                         # 항 합계
        col_sum = 0                         # 열 합계
        for col in range(M):                # 열 반복
            row_sum += arr[row][col]        # 한 행의 원소 덧셈
            col_sum += arr[col][row]        # 한 열의 원소 덧셈
        diagonal_sum_1 += arr[row][row]     # 대각원소 덧셈
        diagonal_sum_2 += arr[row][(M - 1) - row]   # 대각원소 덧셈
        row_sum_list += [row_sum]           # 리스트에 행 합계 저장
        col_sum_list += [col_sum]           # 리스트에 열 합계 저장
    for i in range(99):                     # 합의 최댓값을 추출
        if row_sum_list[i] > row_sum_list[i+1]:
            row_sum_list[i], row_sum_list[i+1] = row_sum_list[i+1], row_sum_list[i]
        if col_sum_list[i] > col_sum_list[i+1]:
            col_sum_list[i], col_sum_list[i+1] = col_sum_list[i+1], col_sum_list[i]
    max_sum_list = [row_sum_list[-1], col_sum_list[-1], diagonal_sum_1, diagonal_sum_2]  # 행, 열, 대각원소의 합의 최댓값 리스트에 저장
    for j in range(3):                      # 최댓값들 중 가장 큰 값을 구함
        if max_sum_list[j] > max_sum_list[j+1]:
            max_sum_list[j], max_sum_list[j+1] = max_sum_list[j+1], max_sum_list[j]
    print(f'#{N} {max_sum_list[-1]}')       # output 출력
