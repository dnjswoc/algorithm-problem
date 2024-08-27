# 17:30 -
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def is_valid(row, col, visited):    # 놓을 수 있는 자리인지 확인하는 함수
    for i in range(row):
        for j in range(N):
            if visited[i][j] == 1 and j == col:  # i행, j열에 방문한 적 있고, 놓을 열의 위치가 j라면
                return False    # return False
    else:
        return True


def find_combination(row, mat, visited, sum_mat):   # 배열 조합을 찾을 함수
    if row == N:
        sum_arr = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1:  # 방문한 적 있는 위치라면
                    sum_arr += mat[i][j]    # 그 위치의 숫자들의 합을 구함
        sum_mat.append(sum_arr)  # 숫자들의 합을 sum_mat 리스트에 저장
        return sum_mat

    for col in range(N):    # 열을 순회하면서
        if is_valid(row, col, visited):  # 놓을 수 있는 위치이면
            visited[row][col] = 1   # 방문 표시하고
            find_combination(row + 1, mat, visited, sum_mat)    # 다음 행으로 넘어감
            visited[row][col] = 0   # 방문 표시 지우기


for test_case in range(T):
    N = int(input())
    num_matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    sum_matrix = []
    find_combination(0, num_matrix, visited, sum_matrix)
    print(f'#{test_case + 1} {min(sum_matrix)}')