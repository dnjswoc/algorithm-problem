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


T = int(input())        # 테스트 케이스 입력

for test_case in range(1, T+1):             # 테스트 케이스만큼 반복
    N, M = map(int, input().split())        # N:정수의 개수 M:합하는 이웃한 값 개수
    arr = list(map(int, input().split()))
    i=0                                     # 초기 index
    max_v=0
    min_v=0
    while i+M <= N:                         # 인덱스가 넘어가기 전까지 순회
        sum=0 #더한값
        for j in range(M):                  # M만큼 순회하면서 값 더하기
            sum +=arr[i+j]
        if max_v < sum:                     # sum이 max보다 클경우 교체
            max_v=sum
            if i==0:                        # 처음의 경우 sum값 무조건 min_v에 들어가도록 예외처리
                min_v=sum
        elif min_v > sum:                   # sum이 min보다 작을경우 교체
            min_v = sum
        i +=1
    print(f'#{test_case} {max_v-min_v}')

