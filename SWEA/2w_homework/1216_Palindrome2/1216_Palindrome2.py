import sys
sys.stdin = open('input.txt', 'r')


def col_list(row, col, max_num):
    new_list = []
    for k in range(max_num):
        new_list.append(char_arr[k + col][row])
    return new_list


def longest_palindrome(max_num, window_size):
    while max_num > 1:
        for i in range(100):
            for j in range(window_size):
                check_list_row = char_arr[i][0 + j:max_num + j]
                check_list_col = col_list(i, j, max_num)
                # check_list_col = char_arr[0 + j:max_num + j][i]
                if check_list_row == check_list_row[::-1] or check_list_col == check_list_col[::-1]:
                    return max_num
        max_num -= 1
        window_size += 1
    return 1


for test_case in range(10):                          # 1
    N = int(input())
    char_arr = [list(input()) for _ in range(100)]    # 8
    max_num = len(char_arr)
    window_size = 1
    answer = longest_palindrome(max_num, window_size)
    print(f'#{N} {answer}')


