swap = {1 : 2 , 2 : 1}

T = int(input())  # 테스트 케이스 수

dxy = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]  # 우 하 좌 상 시계방향으로 8방향 탐색

for case in range(1, T+1):
    N, M = map(int,input().split())   # N : 보드의 한변의 길이 / M : 돌을 놓는 횟수
    bw_li = [list(map(int,input().split())) for _ in range(M)]   # 흑돌 놓을 순서 리스트
    board = [[0]*N for _ in range(N)]  # NXN 빈배열 만들기

    for i in range(N//2-1, N//2+1):   # 오셀로 기본 셋팅
        for j in range(N//2-1, N//2+1):
            if i == j:
                board[i][j] = 2
            else:
                board[i][j] = 1

    for col,row,bw in bw_li:
        board[row-1][col-1] = bw
        for dx, dy in dxy:
            nx, ny = row - 1 + dx, col - 1 + dy
            swap_stone = []
            while 0 <= nx < N and 0 <= ny < N and board[nx][ny] != bw and board[nx][ny] != 0:
                # 범위 벗어나지 않고 놓은돌과 같지 않을때까지
                swap_stone.append([nx, ny])  # 돌 바꿔줄 좌표 더해주기
                nx, ny = nx + dx, ny + dy
            # if 0 <= nx < N and 0 <= ny < N and board[nx][ny]!=0:
            for x,y in swap_stone:
                board[x][y] = bw
    b_count = 0
    w_count = 0
    print(f'#{case}', end=' ')
    for a in board:
        b_count += a.count(1)
        w_count += a.count(2)
    print(f'{b_count} {w_count}')