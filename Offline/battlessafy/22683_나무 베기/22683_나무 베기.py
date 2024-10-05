T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    map_arr = [list(input().split()) for _ in range(N)]