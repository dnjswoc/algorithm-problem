T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    map_arr = [list(input().split()) for _ in range(N)]
    Q = int(input())
    command_arr = [list(input().split()) for _ in range(Q)]