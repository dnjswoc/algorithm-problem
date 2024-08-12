# import sys
# sys.stdin = open('input.txt')

T = 10                                  # 테스트 케이스

dxy = [[1, 0], [0, -1], [0, 1]]         # 델타 검색(행, 열)


def search_ladder(x, y):                # 답이 나오는 사다리를 찾는 함수 정의
    visited = [[0] * block_size for _ in range(block_size)]  # 방문했던 흔적을 남기기 위한 빈 리스트 생성
    visited[x][y] = 1                   # 시작하는 위치를 1로 설정

    while x != block_size - 1:          # 사다리 끝에 도착하는 행까지 반복
        for dx, dy in dxy:              # 델타 검색
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= block_size or ny < 0 or ny >= block_size:    # 유효하지 않은 인덱스 걸러내기
                continue
            if not data[nx][ny]:        # data에 0(사다리가 아님)이면 걸러내기
                continue
            if visited[nx][ny]:         # 이미 방문한 곳이라면 걸러내기
                continue
            visited[x][y] = 1           # 위 조건에 해당하지 않는(방문한 적 없는 사다리) 경우에는 visited 리스트에 1 저장
            x, y = nx, ny               # 이동할 위치로 현 좌표에서 옮김 
    if data[x][y] == 2:                 # 반복이 끝나고 도착한 지점에 2가 있으면
        return True                     # True return
    return False                        # 아니면 False return


for test_case in range(T):              # 테스트 케이스만큼 반복
    N = int(input())                    # 테스트 케이스 입력
    block_size = 100                    # 100X100의 사다리 크기
    data = [list(map(int, input().split())) for _ in range(block_size)]  # 사다리 입력
    for j in range(block_size):         # 출발할 사다리 반복
        if data[0][j] == 0:             # 1이 있는 곳에서 사다리 시작
            continue
        if search_ladder(0, j):         # 도착하는 곳과 연결된 사다리를 찾는 함수 호출
            result = j                  # 찾으면 result에 j를 저장하고
            break                       # 반복문 탈출
    print(f'#{test_case+1} {result}')   # output 출력

