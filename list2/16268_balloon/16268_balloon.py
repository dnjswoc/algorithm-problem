T = int(input())                            # 테스트 케이스 입력

di = [0, 1, 0, -1]                          # 델타 탐색(행)
dj = [1, 0, -1, 0]                          # 델타 탐색(열)

for test_case in range(T):                  # 테스트 케이스만큼 반복
    N, M = map(int, input().split())          # 행, 열 크기 입력
    num_arr = [list(map(int, input().split())) for _ in range(N)]   # 행렬 입력
    max_balloon = 0                         # 최대 꽃가루 수
    for row in range(N):                    # 행 반복
        for col in range(M):                # 열 반복
            balloon = num_arr[row][col]     # 가운데 꽃가루 수 
            for k in range(4):              # 델타 검색
                ni = row + di[k]            # 행
                nj = col + dj[k]            # 열
                if 0 <= ni < N and 0 <= nj < M:     # 행렬 밖으로 넘어가는 인덱스 처리
                    balloon += num_arr[ni][nj]      # 꽃가루 수 덧셈
            if max_balloon < balloon:               # 최대 꽃가루 수 찾기
                max_balloon = balloon
    print(f'#{test_case+1} {max_balloon}')  # output 출력
