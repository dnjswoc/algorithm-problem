import sys
sys.stdin = open('input.txt')

T = int(input())                                # 테스트 케이스 입력

di = [0, -1, -1, -1, 0, 1, 1, 1]                # 델타 탐색(행)
dj = [1, 1, 0, -1, -1, -1, 0, 1]                # 델타 탐색(열)

for test_case in range(T):                      # 테스트 케이스만큼 반복
    N, M = map(int, input().split())            # 행, 열 입력
    area_arr = [list(map(int, input().split())) for _ in range(N)]  # 행렬 입력
    landing_area = 0                            # 예비 후보지 개수 초기화
    for row in range(N):                        # 행 반복
        for col in range(M):                    # 열 반복
            low_area_count = 0                  # 착륙지 높이보다 낮은 지역 개수 초기화
            for delta in range(8):              # 델타 탐색
                ni = row + di[delta]
                nj = col + dj[delta]
                if 0 <= ni < N and 0 <= nj < M:  # 유효한 인덱스만 계산하도록 처리
                    if area_arr[row][col] > area_arr[ni][nj]:   # 착륙지 높이보다 델타 탐색한 주변 지역 높이가 낮으면
                        low_area_count += 1     # 착륙지 높이보다 낮은 지역 개수 1추가
            if low_area_count >= 4:             # 착륙지 높이보다 낮은 지역의 개수가 4 이상이면
                landing_area += 1               # 예비 후보지 개수 1추가
    print(f'#{test_case+1} {landing_area}')     # output 출력
