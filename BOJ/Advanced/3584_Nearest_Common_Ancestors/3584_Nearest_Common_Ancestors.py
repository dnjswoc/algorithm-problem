T = int(input())

for test_case in range(T):
    N = int(input())
    edge_arr = [list(map(int, input().split())) for _ in range(N - 1)]
    node_a, node_b = map(int, input().split())
    adjL = [[] for _ in range(N + 1)]

    for arr in edge_arr:
        adjL[arr[0]].append(arr[1])
    print(adjL)
