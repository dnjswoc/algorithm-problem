# 17:30 -
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def is_valid(row, col, visited):
    for i in range(row):
        for j in range(N):
            if visited[i][j] == 1 and j == col:
                return False
    else:
        return True


def find_combination(row, mat, visited, sum_mat):
    if row == N:
        sum_arr = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1:
                    sum_arr += mat[i][j]
        sum_mat.append(sum_arr)
        return min(sum_mat)

    for col in range(N):
        if is_valid(row, col, visited):
            visited[row][col] = 1
            find_combination(row + 1, mat, visited, sum_mat)
            visited[row][col] = 0


for test_case in range(T):
    N = int(input())
    num_matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    sum_matrix = []
    find_combination(0, num_matrix, visited, sum_matrix)
    print(f'#{test_case + 1} {min(sum_matrix)}')