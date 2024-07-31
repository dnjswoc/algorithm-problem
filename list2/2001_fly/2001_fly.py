T = int(input())                        # 테스트 케이스 입력

for i in range(T):                      # 테스트 케이스만큼 반복
    N, M = map(int, input().split())    # N*N행렬의 크기와 M*M 파리채의 크기 입력
    arr = [list(map(int, input().split())) for _ in range(N)]   # N*N 행렬 입력
    max_kill = 0                        # 잡을 수 있는 파리의 최댓값 변수 생성
    Window_number = N - M + 1           # 윈도우 크기 계산
    for j in range(Window_number):      # 윈도우 크기만큼 반복
        for k in range(Window_number):  # 윈도우 크기만큼 반복
            kill = 0                    # 해당 윈도우에서 잡는 파리 수의 변수
            for p in range(M):
                for q in range(M):
                    kill += arr[j+p][k+q]   # 해당 윈도우에서의 잡는 파리의 수 계산
            if max_kill < kill:         # 잡을 수 있는 파리의 최댓값 계산
                max_kill = kill
    print(f'#{i+1} {max_kill}')         # output 출력
