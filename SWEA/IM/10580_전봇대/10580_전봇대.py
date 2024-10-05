# 17:00 - 17:20
# 20:55 - ...

'''
전봇대의 전선의 교점을 구하는 문제입니다.
왼쪽 전봇대의 A점부터 시작하여 오른족 전봇대의 B점으로 도착하는 입력값들이 주어졌습니다.
전선 두개를 비교하여 (A, A'), (B, B')가 있다고 보면
왼쪽 전봇대에서 출발하는 A점의 값을 다음 전선의 A'점과 비교하여 작은 상황에서
오른쪽 전봇대에 도착할 때는 B점의 값이 B'점보다 커지면 교점이 생긴다고 생각하고 문제에 접근했습니다.
하지만 답을 제출할 때마다 15개 중 5만 맞아서 멘탈이 많이 무너졌는데
나영님의 예리한 의견을 통해
저는 입력한 순서대로만 하다보니 계속 A가 A'보다 크고, B가 B'보다 작은 상황은 생각하지 못하였던 것이었습니다ㅎㅎ
그래서 입력받은 값을 A점들을 기준으로 정렬하고 나니 문제가 풀렸습니다~~
이상입니다~~
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    line_arr = [list(map(int, input().split())) for _ in range(N)]
    intersection = 0    # 교점 개수
    for a in range(N - 1, 0, -1):   # 출발하는 점을 기준으로 정렬
        for b in range(a):
            if line_arr[b][0] > line_arr[b + 1][0]:
                line_arr[b], line_arr[b + 1] = line_arr[b + 1], line_arr[b]

    for i in range(len(line_arr) - 1):  # N - 1만큼 반복
        for j in range(i + 1, len(line_arr)):   # i 뒤에 나오는 값들의 출발점과 끝점을 비교해서
            if line_arr[i][0] < line_arr[j][0] and line_arr[i][1] > line_arr[j][1]:
                intersection += 1   # 출발점이 작은 상태에서 끝점에서 커진 상태로 끝나면 교점이 생긴다.
    print(f'#{test_case + 1} {intersection}')

