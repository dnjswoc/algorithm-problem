arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]   # 1부터 12까지의 숫자를 원소로 가진 집합 A

n = 12                                          # 집합 A의 길이
T = int(input())                                # 테스트 케이스 입력
for test_case in range(T):                      # 테스트 케이스만큼 반복
    N, K = map(int, input().split())            # N : 부분집합의 크기, K : 부분집합 원소의 합
    subset_count = 0                            # 부분집합 원소의 합이 K와 일치하는지 계산
    for i in range(1, 1 << 12):                 # 집합 A의 부분집합 구하기(8~14번 줄)
        factor_list = []                        # 부분집합의 원소를 넣을 리스트
        factor_list_count = 0                   # 부분집합의 크기를 셀 변수 초기화
        for j in range(12):
            if i & (1 << j):
                factor_list += [arr[j]]         # 부분집합 원소를 factor_list에 저장
                factor_list_count += 1          # 부분집합 크기 계산
        sum_list = 0                            # 부분집합 원소의 합 구하기
        if factor_list_count == N:              # 부분집합의 크기가 N과 같으면
            for k in range(N):                  # N만큼 반복
                sum_list += factor_list[k]      # 부분집합 원소를 합한다.
            if sum_list == K:                   # 부분집합 원소의 합이 K와 같으면
                subset_count += 1               # subset_count를 1씩 증가
    print(f'#{test_case+1} {subset_count}')     # output 출력

