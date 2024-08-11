import sys
sys.stdin = open('sample_input.txt', 'r')

for test_case in range(1):                          # 1
    N = int(input())
    char_arr = [list(input()) for _ in range(8)]    # 8
    max_num = len(char_arr)
    window_size = 0
    palindrome = 1
    while max_num > 1:
        for i in range(8):
            for j in range(window_size):
                check_list_row = char_arr[i][0 + j:max_num + j]
                # check_list_col = char_arr[0 + j:max_num + j][i]
                if check_list_row == check_list_row[::-1]:
                    palindrome = max_num
                    break
        max_num -= 1
        window_size += 1
    print(palindrome)


