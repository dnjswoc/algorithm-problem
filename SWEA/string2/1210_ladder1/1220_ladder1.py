import sys
sys.stdin = open('input.txt')


def ladder(arr, arr_point):             # 사다리의 도착점이 출발하는 지점을 찾는 함수 정의
    i = block_size - 1                  # i : 99번째 행
    j = arr_point                       # j : 사다리가 도착하는 지점의 열
    dij = [[0, -1], [0, 1], [-1, 0]]    # 좌, 우, 상 델타 탐색
    while i > 0:                        # i가 0이 될 때 까지(도착할 때 까지)
        for di, dj in dij:              # 델타 탐색
            ni = i+di
            nj = j+dj
            if ni < 0 or ni >= block_size or nj < 0 or nj >= block_size:    # 유효한 인덱스가 아니면 예외 처리
                continue
            if arr[ni][nj] == 1:        # 사다리가 있다면
                arr[i][j] = 0           # 지나왔던 곳의 사다리 지우기
                i = ni                  # 위치했던 사다리에서 다음 사다리로 인덱스 위치를 옮김
                j = nj
    return j                            # 맨 위 행에 도착했을 때의 열의 값을 return


for test_case in range(10):             # 테스트 케이스 반복
    tc = int(input())                   # 테스트 케이스 넘버 입력
    block_size = 100                    # 행렬의 크기는 100
    ladder_arr = [list(map(int, input().split())) for _ in range(block_size)]   # 행렬(사다리) 입력
    arrive_point = 0                    # 사다리가 도착한 위치
    for j in range(block_size):         # 사다리가 도착한 위치의 열의 값 찾기
        if ladder_arr[-1][j] == 2:
            arrive_point = j
    start_point = ladder(ladder_arr, arrive_point)  # 사다리가 출발하는 곳의 위치 찾는 함수 호출
    print(f'#{tc} {start_point}')       # output 출력
