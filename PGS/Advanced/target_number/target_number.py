# import sys
# sys.stdin = open('input.txt', 'r')
#
# T = int(input())
#
#
# def target_number(num, numbers, target):
#     global cnt
#     if num == len(numbers):
#         if sum(numbers) == target:
#             cnt += 1
#         return
#     if sum(numbers) < target:
#         return
#     for i in [-1, 1]:
#         numbers[num] *= i
#         target_number(num + 1, numbers, target)
#         numbers[num] *= i
#
#
# for test_case in range(1, T + 1):
#     numbers = list(map(int, input().split()))
#     target = int(input())
#     cnt = 0
#     target_number(0, numbers, target)
#     print(cnt)

# 프로그래머스 수정 코드

# answer = 0
#
#
# def solution(numbers, target):
#     target_number(0, numbers, target)
#     return answer
#
#
# def target_number(num, numbers, target):
#     global answer
#
#     if num == len(numbers):
#         if sum(numbers) == target:
#             answer += 1
#         return
#     if sum(numbers) < target:
#         return
#
#     for i in [-1, 1]:
#         numbers[num] *= i
#         target_number(num + 1, numbers, target)
#         numbers[num] *= i

# 나영이 코드
from collections import deque

def solution(numbers, target):
    answer = 0
    idx = -1  # 인덱스
    hap = 0  # 합 값 담아줌
    queue = deque()
    queue.append(idx)
    queue.append(hap)

    while queue:
        i, v = queue.popleft(), queue.popleft()
        i += 1
        if i == len(numbers) and target == v:
            answer += 1
        if i >= len(numbers):
            continue
        else:
            queue.append(i)
            queue.append(numbers[i] + v)
            queue.append(i)
            queue.append(v - numbers[i])

    return answer

print(solution([4, 1, 2, 1], 4))