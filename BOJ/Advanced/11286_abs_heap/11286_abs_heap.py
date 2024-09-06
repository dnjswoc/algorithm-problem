import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappush, heappop


# def enq(n):
#     global last
#     last += 1
#     h[last] = n
#     c = last
#     p = c // 2
#     while p >= 1 and abs(h[p]) >= abs(h[c]):
#         if abs(h[p]) == abs(h[c]) and h[p] < h[c]:
#             continue
#         h[p], h[c] = h[c], h[p]
#         c = p
#         p = c // 2
#
#
# def deq():
#     global last
#     tmp = h[1]
#     h[1] = h[last]
#     last -= 1
#     p = 1
#     c = p * 2
#     while c <= last:
#         if c + 1 <= last and abs(h[c]) >= abs(h[c + 1]):
#             if abs(h[c]) == abs(h[c + 1]) and h[c] < h[c + 1]:
#                 c = c
#             else:
#                 c += 1
#         if abs(h[p]) >= abs(h[c]):
#             if abs(h[p]) == abs(h[c]) and h[p] < h[c]:
#                 continue
#             h[p], h[c] = h[c], h[p]
#             p = c
#             c = p * 2
#         else:
#             break
#     return tmp
#
#
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# # print(arr)
# h = [0] * (N + 1)
# last = 0
# for num in arr:
#     if num:
#         enq(num)
#         continue
#     if last == 0:
#         print(0)
#     else:
#         print(deq())

N = int(input())
arr = [int(input()) for _ in range(N)]

heap = []

for num in arr:
    if num:
        heappush(heap, num)
        continue
    if not heap:
        print(0)
        continue
    print(heappop(heap))
