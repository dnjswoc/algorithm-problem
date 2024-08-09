import sys
sys.stdin = open('input.txt')

T = int(input())

dij = [[-1, 0], [0, 1], [1, 0], [0, -1]]            # 델타 탐색

# class Counter:
#     def __init__(self):
#         self.cnt =0


def maze_check(row, col, visited):                  # 미로가 성립하는지 확인하는 함수 정의
    global result                                   # 전역변수 선언하여 result 값 저장
    visited[row][col] = 1                           # 넘겨 받은 위치를 방문 표시
    for di, dj in dij:                              # 델타 탐색
        ni = row + di
        nj = col + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= N:  # 유효하지 않은 인덱스 continue
            continue
        if maze_arr[ni][nj] == end_value:           # 도착점을 찾으면 return 1
            result = 1
            # cnt_instance.cnt = 1
            return
        if maze_arr[ni][nj] == 0 and visited[ni][nj] == 0:  # 델타 탐색 도착점을 못찾고 0만 있고, 방문한 적이 없으면
            maze_check(ni, nj, visited)             # 그 위치에서 maze_check 함수 호출

    return                                          # 도착점을 못 찾은 채로 함수 return


for test_case in range(T):
    N = int(input())
    maze_arr = [list(map(int, input())) for _ in range(N)]
    end_value = 3                                   # 도착점
    result = 0                                      # result 변수 생성
    visited = [[0] * N for _ in range(N)]
    # cnt_instance = Counter()
    for row in range(N):                            # 시작 지점 찾는 반복문
        for col in range(N):
            if maze_arr[row][col] == 2:
                start_idx_row = row
                start_idx_col = col
                # cnt_instance.cnt
    maze_check(start_idx_row, start_idx_col, visited)   # 미로가 성립하는지 함수로 확인
    print(f'#{test_case+1} {result}')               # 함수 결과 출력
