import sys
sys.stdin = open('sample_input.txt', 'r')


def palindrome_check():
    for i in range(8):
        if char_arr[i][0:9] == char_arr[i][8:-1:-1]:
            return 8
        elif char_arr[0:9][i] == char_arr[8:-1:-1][i]:
            return 8
    else:
        return -1


for test_case in range(1):                          # 1
    N = int(input())
    char_arr = [list(input()) for _ in range(8)]    # 8
    # print(palindrome_check())
    for i in range(8):
        check_list = char_arr[i][0:9]


