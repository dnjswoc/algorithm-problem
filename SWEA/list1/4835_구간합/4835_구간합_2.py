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
