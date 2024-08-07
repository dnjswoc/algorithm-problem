# import sys
# sys.stdin = open('input.txt')

T = int(input())


def snail_matrix(matrix):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    num = 1
    i, j = 0, 0
    visited = [[0] * N for _ in range(N)]
    delta = 0
    while num <= 7:
        # visited[i][j] = 1
        matrix[i][j] = num
        ni = i + di[delta]
        nj = j + dj[delta]
        print(i, j)
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            if ni == N:
                ni -= 1
            elif nj == N:
                nj -= 1
            delta += 1
            if delta == 4:
                delta -= 4

        i = ni
        j = nj
        num += 1

    return matrix


for test_case in range(T):
    N = int(input())
    num_matrix = [[0] * N for _ in range(N)]
    new_matrix = snail_matrix(num_matrix)
    for row in range(N):
        for col in range(N):
            print(new_matrix[row][col], end=' ')
        print()

