T = int(input())                            # 테스트 케이스 입력
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]   # 정렬된 리스트(1~9)
di = [0, 1, 1, 1, 0, -1, -1, -1]            # 델타 탐색(행)
dj = [1, 1, 0, -1, -1, -1, 0, 1]            # 델타 탐색(열)


def list_sort(num_list):                    # 버블 정렬로 리스트를 정렬할 함수
    for i in range(8, 0, -1):
        for j in range(0, i):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


for test_case in range(T):                  # 테스트 케이스만큼 반복
    Sudoku = [list(map(int, input().split())) for _ in range(9)]    # 스도쿠 입력
    result = 0                              # 스도쿠 규칙에 맞는지 확인할 변수
    for row in range(9):                    # 행 반복
        row_list = []                       # 행 리스트 생성
        col_list = []                       # 열 리스트 생성
        for col in range(9):                # 열 반복
            if (row - 1) % 3 == 0 and (col - 1) % 3 == 0:   # 스도쿠 3X3 1칸 추출을 위한 조건문
                matrix_list = [Sudoku[row][col]]
                for delta in range(8):      # 델타 탐색을 위한 반복
                    ni = row + di[delta]
                    nj = col + dj[delta]
                    matrix_list += [(Sudoku[ni][nj])]
                matrix_list = list_sort(matrix_list)    # 스도쿠 3X3 1칸 정렬
                if matrix_list == sorted_list:  # 정렬된 스도쿠가 sorted_list와 같은지 확인
                    result += 1             # 같으면 result 1씩 증가
            col_list += [Sudoku[row][col]]  # 열 리스트 저장
            row_list += [Sudoku[col][row]]  # 행 리스트 저장
        col_list = list_sort(col_list)      # 열 리스트 정렬
        row_list = list_sort(row_list)      # 행 리스트 정렬
        if col_list == row_list == sorted_list: # 정렬된 열 리스트와 행 리스트가 sorted_list와 같은지 확인
            result += 1                     # 같으면 result 1씩 증가
    if result == 18:                        # result가 18이라면
        print(f'#{test_case + 1} {1}')      # 스도쿠 완성으로 1 출력
    else:
        print(f'#{test_case + 1} {0}')      # 그렇지 않으면 0 출력
