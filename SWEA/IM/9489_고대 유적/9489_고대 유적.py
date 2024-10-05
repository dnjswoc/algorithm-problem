# 15:40 - 16:50

'''
땅 속에 묻혀있는 고대 유적이 가로, 세로 방향만 있으므로 [오른쪽, 아래쪽] 델타 탐색을 하여
연속된 1의 개수가 가장 많은 값을 찾으면 되겠다고 생각하고 문제를 풀었습니다.
'''

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
            for di, dj in dij:  # 델타 탐색
                ni = row + di
                nj = col + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= M:  # 유효하지 않은 인덱스 제외
                    continue
                if not relic_arr[row][col]:  # 0이면 제외
                    continue
                count_relic = 1  # 1이 하나만 있어도 유적의 크기는 1이 되는 것이므로
                while relic_arr[ni][nj]:   # 1일 때(유적이 있을 때)까지만 반복
                    count_relic += 1
                    if ni + di < 0 or ni + di >= N or nj + dj < 0 or nj + dj >= M:  # 다음으로 갈 인덱스가 유효하지 않으면 제외
                        break
                    ni += di
                    nj += dj
                if max_relic < count_relic:  # 가장 큰 유적의 크기를 구함
                    max_relic = count_relic
    print(f'#{test_case+1} {max_relic}')

