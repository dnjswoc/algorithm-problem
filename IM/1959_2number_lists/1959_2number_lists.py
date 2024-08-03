T = int(input())                                    # 테스트 케이스 입력


def compare_lists(list_1, list_2, num_1, num_2):    # 윈도우 개수와 윈도우 크기의 리스트를 반환하는 함수 정의
    window_list = []                                # 숫자열의 개수가 적은 리스트의 크기와 동일한 크기의 윈도우를 저장할 리스트 생성
    if num_1 > num_2:                               # N이 크면
        win_size = num_1 - num_2 + 1                # 윈도우 개수는 N - M + 1
        for i in range(win_size):                   # 윈도우 개수만큼 반복
            window_list += [list_1[0+i:num_2+i]]    # 윈도우를 돌아가며 숫자열의 개수가 큰 리스트를 차례로 저장
    else:                                           # M이 크면
        win_size = num_2 - num_1 + 1                # 윈도우 개수는 M - N + 1
        for i in range(win_size):
            window_list += [list_2[0+i:num_1+i]]
    return window_list, win_size                    # 숫자열의 개수가 큰 리스트에서 추출한 윈도우 크기의 리스트들과 윈도우 개수 return


def multiple_list(list_1, list_2, num_1, num_2, com_list, win_size):    # 리스트를 돌아가며 곱해서 더한 값의 최댓값을 반환하는 함수 정의
    multiple_factor = []                            # 곱해서 나온 값을 저장할 빈 리스트 생성
    for i in range(win_size):                       # 윈도우 개수만큼 반복
        sum_multiple = 0                            # 곱셈 값을 더할 변수 생성
        if num_1 > num_2:                           # N이 크면
            for j in range(num_2):                  # M만큼 반복
                multiple = list_2[j] * com_list[i][j]   # 숫자열이 큰 리스트에서 추출한 리스트들과 숫자열이 작은 리스트 인덱스끼리 곱함
                sum_multiple += multiple            # 곱한 값을 더해줌

        else:                                       # M이 크면
            for j in range(num_1):                  # N만큼 반복
                multiple = list_1[j] * com_list[i][j]
                sum_multiple += multiple
        multiple_factor += [sum_multiple]           # 곱하여 더한 값들을 리스트에 저장
    max_multiple_factor = multiple_factor[0]        # 최댓값을 구할 변수를 리스트이 0번째 인덱스로 초기화
    for k in range(win_size-1):                     # 윈도우 개수 -1만큼 반복하여 최댓값 계산
        if max_multiple_factor < multiple_factor[k+1]:
            max_multiple_factor = multiple_factor[k+1]
    return max_multiple_factor                      # 최댓값 return


for test_case in range(T):                          # 테스트 케이스만큼 반복
    N, M = map(int, input().split())                # N, M 입력
    A_list = list(map(int, input().split()))        # 숫자열 입력
    B_list = list(map(int, input().split()))
    compare_list, window_size = compare_lists(A_list, B_list, N, M)  # 윈도우를 통해 추출한 리스트와 윈도우 개수 구하는 함수 호출 
    max_multiple = multiple_list(A_list, B_list, N, M, compare_list, window_size)   # 곱하여 더해 구한 값 중 최댓값 구하는 함수 호출
    print(f'#{test_case+1} {max_multiple}')         # output 출력
