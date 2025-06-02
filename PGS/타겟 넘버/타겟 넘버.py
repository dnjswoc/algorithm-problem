# import sys
# sys.stdin = open('input.txt', 'r')

'''
배열이 주어지고 배열의 원소들에 -1을 곱하면서
target이 되는 조합을 찾으면 되겠다 생각하고 문제에 접근했습니다.
numbers = [1, 1, 1, 1, 1]
target = 3
combination
[-1, 1, 1, 1, 1]
[1, -1, 1, 1, 1]
[1, 1, -1, 1, 1]
[1, 1, 1, -1, 1]
[1, 1, 1, 1, -1]
return = 5
'''

T = int(input())


def target_number(num, numbers, target):
    global cnt
    if num == len(numbers):
        if sum(numbers) == target:
            cnt += 1
        return
    if sum(numbers) < target:
        return
    for i in [-1, 1]:
        numbers[num] *= i
        target_number(num + 1, numbers, target)
        numbers[num] *= i


for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    target = int(input())
    cnt = 0
    target_number(0, numbers, target)
    print(cnt)

# 프로그래머스 수정 코드

answer = 0


def solution(numbers, target):
    target_number(0, numbers, target)
    return answer


def target_number(num, numbers, target):
    global answer

    if num == len(numbers):  # 인덱스가 배열의 길이과 같아지고 리스트의 합이 target과 같으면
        if sum(numbers) == target:
            answer += 1     # answer + 1
        return
    # 재귀로 돌아가다 리스트의 합이 target 보다 작으면 return
    # (-1이나 1이 곱해져 재귀로 돌아가면 리스트의 합이 작거나 같아질 경우 밖에 없기 때문에)
    if sum(numbers) < target:
        return

    for i in [-1, 1]:   # -1과 1을 번갈아 곱해주면서 재귀로 target을 찾아간다.
        numbers[num] *= i   # -1이나 1을 numbers 해당 인덱스에 곱해주고
        target_number(num + 1, numbers, target)  # 다음 인덱스를 넘겨주며 재귀
        numbers[num] *= i   # -1이나 1을 다시 곱해줘 원상복구

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