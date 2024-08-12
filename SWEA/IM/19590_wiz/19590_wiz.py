# N = int(input())
# area_list = [list(map(int, input().split())) for _ in range(N)]
# K = int(input())
#
# di = [-1, -1, 1, 1]
# dj = [-1, 1, 1, -1]
#
# max_sum_monster = 0
#
# for row in range(N):
#     for col in range(N):
#         sum_monster = 0
#         for delta in range(4):
#             for k in range(1, K+1):
#                 ni = row + di[delta]*k
#                 nj = col + dj[delta]*k
#                 if 0 <= ni < N and 0 <= nj < N:
#                     sum_monster += area_list[ni][nj]
#         if max_sum_monster < sum_monster:
#             max_sum_monster = sum_monster
# print(max_sum_monster)
print(list(range(4, 0, -1)))
