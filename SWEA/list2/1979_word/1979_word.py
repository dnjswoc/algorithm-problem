import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())
    puzzle_arr = [list(map(int, input().split())) for _ in range(N)]
    correct_list = [1] * K
    word_count = 0
    check_arr = []  # 단어가 들어갈 수 있는 리스트 입력
    for row in range(N):    # 행 단위로 검색
        check_arr_r = []
        for col in range(N):
            if puzzle_arr[row][col]:    # 행렬의 값이 1이라면
                check_arr_r.append(puzzle_arr[row][col])    # 리스트에 저장
            elif not puzzle_arr[row][col]:  # 0이라면
                check_arr.append(check_arr_r)   # 1을 저장했던 리스트를 단어가 들어갈 수 있는 check_arr 리스트에 넣고
                check_arr_r = []        # check_arr_r 리스트를 초기화
        check_arr.append(check_arr_r)   # 열에 대한 순회가 끝나면 마지막까지 check_arr_r 리스트에 저장된 값을 check_arr 리스트에 저장
    for col in range(N):    # 열 단위로 검색
        check_arr_c = []
        for row in range(N):
            if puzzle_arr[row][col]:
                check_arr_c.append(puzzle_arr[row][col])
            elif not puzzle_arr[row][col]:
                check_arr.append(check_arr_c)
                check_arr_c = []
        check_arr.append(check_arr_c)
    for arr in check_arr:
        if arr == correct_list:
            word_count += 1
    print(f'#{test_case+1} {word_count}')

