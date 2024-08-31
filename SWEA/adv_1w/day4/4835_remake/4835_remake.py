import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num_arr = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0

    for i in range(N):  # 가장 긴 행의 길이를 구하기 위한 반복문
        if max_len <= len(num_arr[i]):
            max_len = len(num_arr[i])

    for i in range(N):  # 가장 긴 행의 길이보다 행의 길이가 짧으면 그만큼 -1을 채운다.
        while len(num_arr[i]) < max_len:
            num_arr[i].append(-1)

    transpose = []  # -1을 채운 행렬의 전치행렬을 구하여 각 행에서 -1보다 큰 값들만 고른다. ex) [5 1 1 1 9], [3, 2, 2, 0], ...
    for col in range(max_len):  # 가장 긴 행의 길이만큼 반복
        col_lst = []    # 열마다 0보다 크거나 같은 값을 저장한다.
        for row in range(N):
            if num_arr[row][col] >= 0:
                col_lst.append(num_arr[row][col])
        if len(col_lst) < M:    # 만약 열에서 0보다 크거나 같은 값이 M개보다 작으면 구간합을 구할 수 없으므로 버린다.
            continue
        transpose.append(col_lst)   # 열에서 0보다 크거나 같은 값이 M개 이상이면 transpose에 저장

    if not transpose:   # transpose가 비어있으면(열에서 0보다 크거나 같은 값이 M개 이상인 경우가 없으면)
        answer = -1  # -1 출력
    else:
        max_sum = sum(transpose[0][0:M])    # 첫 번째 구간합을 max_sum, min_sum 으로 초기화
        min_sum = sum(transpose[0][0:M])
        for arr in transpose:   # 각 열에서 0보다 크거나 같은 값을 저장한 리스트를 하나씩 반복하며
            for k in range(len(arr) - M + 1):   # 이웃한 M개의 숫자를 돌아가며 구간합을 구한다.
                sum_lst = sum(arr[k:k+M])
                if max_sum <= sum_lst:  # 그 값이 max_sum보다 크면 max_sum 재할당
                    max_sum = sum_lst
                if min_sum >= sum_lst:  # 그 값이 min_sum보다 작으면 min_sum 재할당
                    min_sum = sum_lst
        answer = max_sum - min_sum

    print(f'#{test_case} {answer}')
