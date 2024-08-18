# 15:40 - 16:50
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

dij = [[0, 1], [1, 0]]  # 오른쪽, 아래 방향으로만 탐색

for test_case in range(T):
    N, M = map(int, input().split())
    relic_arr = [list(map(int, input().split())) for _ in range(N)]
    max_relic = 0   # 최댓값
    for row in range(N):    # 행 반복
        for col in range(M):    # 열 반복
            for di, dj in dij:
                ni = row + di
                nj = col + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                if not relic_arr[row][col]:
                    continue
                count_relic = 1
                while relic_arr[ni][nj]:   # 1일 때(유물이 있을 때)까지만 반복
                    count_relic += 1
                    if ni + di < 0 or ni + di >= N or nj + dj < 0 or nj + dj >= M:
                        break
                    ni += di
                    nj += dj
                if max_relic < count_relic:
                    max_relic = count_relic
    print(f'#{test_case+1} {max_relic}')

