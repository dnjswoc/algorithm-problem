T = int(input())                                # 테스트 케이스 입력

di = [0, 1, 0, -1]                              # 델타 탐색(행)
dj = [1, 0, -1, 0]                              # 델타 탐색(열)

for test_case in range(T):                      # 테스트 케이스만큼 반복
    N, M = map(int, input().split())            # 행, 열 입력
    num_arr = [list(map(int, input().split())) for _ in range(N)]   # 행렬 입력
    max_sum_balloon = 0                         # 최대 꽃가루 합 변수 생성
    for row in range(N):                        # 행 반복
        for col in range(M):                    # 열 반복
            sum_balloon = num_arr[row][col]     # 꽃가루 합 구하기(초깃값 : 가운데 값)
            for delta in range(4):              # 델타 탐색
                ni = row + di[delta]
                nj = col + dj[delta]
                if 0 <= ni < N and 0 <= nj < M:  # 유효한 인덱스만 설정하기
                    sum_balloon += num_arr[ni][nj]  # 사방의 꽃가루 합하기
            if max_sum_balloon < sum_balloon:   # 최대 꽃가루 합 구하기
                max_sum_balloon = sum_balloon
    print(f'#{test_case+1} {max_sum_balloon}')  # output 출력

