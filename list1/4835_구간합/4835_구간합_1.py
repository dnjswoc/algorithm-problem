T = int(input())    # 테스트 케이스 입력

for t in range(T):                              # 테스트 케이스만큼 반복
    N, M = map(int, input().split())            # N(정수의 개수), M(구간의 개수)
    num_list = list(map(int, input().split()))  # N개의 정수 입력
    part_sum_list = [0] * (N - M + 1)           # 구간합들을 받을 리스트 생성
    for cn in range(N - M + 1):                 # 구간합의 개수만큼 반복
        sum_list = 0
        for part in range(M):                   # 구간의 크기만큼 반복
            sum_list += num_list[cn+part]       # 이웃한 정수의 합을 계산
        part_sum_list[cn] = sum_list            # 구간합을 리스트에 저장
    for outer in range(N - M, 0, -1):           # 버블 정렬로 구간합 리스트를 정렬
        for inner in range(0, outer):
            if part_sum_list[inner] > part_sum_list[inner+1]:
                part_sum_list[inner], part_sum_list[inner+1] = part_sum_list[inner+1], part_sum_list[inner]
    answer = part_sum_list[-1] - part_sum_list[0]   # 리스트의 가장 마지막 값에서 첫 번째 값을 뺀다.
    print(f'#{t+1} {answer}')

