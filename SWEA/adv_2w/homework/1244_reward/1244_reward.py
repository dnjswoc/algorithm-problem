


# 색칠하기
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     color_arr = [list(map(int, input().split())) for _ in range(N)]
#     empty_arr = [[0] * 10 for _ in range(10)]
#     color_cnt = 0
#
#     for arr in color_arr:
#         for row in range(arr[0], arr[2] + 1):
#             for col in range(arr[1], arr[3] + 1):
#                 empty_arr[row][col] += 1
#
#     # for i in range(10):
#     #     print(empty_arr[i])
#     for i in range(10):
#         for j in range(10):
#             if empty_arr[i][j] == 2:
#                 color_cnt += 1
#     print(f'#{test_case} {color_cnt}')
