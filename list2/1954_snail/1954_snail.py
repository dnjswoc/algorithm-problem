import sys
sys.stdin = open('input.txt')

T = int(input())


def snail_matrix():
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    num = 1
    i, j = 0, 0
    visited = [[0] * N for _ in range(N)]
    while num <= N**2:
        visited[i][j] = 1
        num_matrix[i][j] = num
        for delta in range(4):
            ni = i + di[delta]
            nj = j + dj[delta]

        num += 1
    pass


for test_case in range(T):
    N = int(input())
    num_matrix = [[0] * N for _ in range(N)]

