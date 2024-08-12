# import sys
# sys.stdin = open('input.txt')

T = int(input())


def snail_matrix(matrix):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i, j = 0, 0
    delta = 0
    for num in range(1, N*(N+1)):
        matrix[i][j] = num

    return matrix


for test_case in range(T):
    N = int(input())
    num_matrix = [[0] * N for _ in range(N)]
    new_matrix = snail_matrix(num_matrix)
    for row in range(N):
        for col in range(N):
            print(new_matrix[row][col], end=' ')
        print()

