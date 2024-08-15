# 17:00 - 17:20
# 20:55 -
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    line_arr = [list(map(int, input().split())) for _ in range(N)]
    intersection = 0    # 교점 개수
    for i in range(len(line_arr) - 1):  # N - 1만큼 반복
        for j in range(i + 1, len(line_arr)):   # i 뒤에 나오는 값들의 출발점과 끝점을 비교해서
            if line_arr[i][0] < line_arr[j][0] and line_arr[i][1] > line_arr[j][1]:
                intersection += 1   # 출발점이 작은 상태에서 끝점에서 커진 상태로 끝나면 교점이 생긴다.
    print(f'#{test_case + 1} {intersection}')
