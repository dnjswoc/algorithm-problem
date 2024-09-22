T = int(input())                        # 테스트 케이스 입력

di = [0, 1, 0, -1]                      # 델타 탐색(행)
dj = [1, 0, -1, 0]                      # 델타 탐색(열)

for test_case in range(T):              # 테스트 케이스만큼 반복
    N, M = map(int, input().split())    # 행, 열 입력
    num_arr = [list(map(int, input().split())) for _ in range(N)]   # 행렬 입력
    max_balloon_sum = 0                 # 최대 꽃가루 수
    for row in range(N):                # 행 반복
        for col in range(M):            # 열 반복
            balloon_sum = num_arr[row][col]     # balloon_sum에 우선 가운데 값 설정
            for delta in range(4):      # 델타 탐색
                for ball in range(1, num_arr[row][col]+1):  # 가운데 값에 따라 늘어나는 간격 반복 설정
                    ni = row + di[delta] * ball     # 델타 탐색(행) * 간격 반복
                    nj = col + dj[delta] * ball     # 델타 탐색(열) * 간격 반복
                    if 0 <= ni < N and 0 <= nj < M:     # 벗어나는 인덱스 조건 처리
                        balloon_sum += num_arr[ni][nj]  # balloon_sum 계산(늘어나는 간격 포함)
            if max_balloon_sum < balloon_sum:       # 최대 꽃가루 수 찾기
                max_balloon_sum = balloon_sum
    print(f'#{test_case+1} {max_balloon_sum}')      # output 출력
