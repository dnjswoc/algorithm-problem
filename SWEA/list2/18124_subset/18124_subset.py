T = int(input())                                # 테스트 케이스 입력


def sum_list(num_list, count):                  # 부분집합 원소의 합을 구하는 함수
    factor_sum = 0
    for c in range(count):                      # 원소 개수만큼 반복
        factor_sum += num_list[c]               # 원소 합 구하여
    return factor_sum                           # 반환


for test_case in range(T):                      # 테스트 케이스만큼 반복
    num_list = list(map(int, input().split()))  # 리스트 입력
    n = 10
    factor_sum_list = []                        # 부분집합 원소의 합을 저장할 빈 리스트 생성
    for i in range(1, 1 << n):                  # 부분집합 구하는 반복문
        factor_list = []                        # 부분집합 원소를  저장할 빈 리스트 생성
        factor_count = 0                        # 부분집합의 크기를 계산할 변수 생성
        for j in range(n):
            if i & (1 << j):
                factor_list += [num_list[j]]    # 부분집합 원소 저장
                factor_count += 1               # 부분집합 크기 계산
        factor_sum = sum_list(factor_list, factor_count)    # 함수 호출하여 부분집합 원소의 합 계산
        factor_sum_list += [factor_sum]         # 부분집합 원소의 합을 리스트에 저장
    if 0 in factor_sum_list:                    # 리스트 중 0이 있으면
        print(f'#{test_case+1} 1')              # 1을 출력
    else:                                       # 없으면
        print(f'#{test_case+1} 0')              # 0 출력
