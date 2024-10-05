'''
문제에 주어진 그림을 보고 홀수 번호의 방과 짝수 번호의 방이 같은 복도를 공유한다는 사실을 깨닫고,
학생이 방에서 나와 다른 방으로 돌아가는 동안 지나치게 되는 복도의 인덱스를 구해서
지나치는 복도의 인덱스가 겹치면 한 타임 기다렸다가 다음 순서에 가야하게 되는겁니다.
겹치는 복도가 없는 학생들은 한꺼번에 돌아갈 수 있으므로 길이가 200인 빈 복도의 배열을 만들어
모든 학생이 복도의 인덱스를 지나가게 될 때마다 +1 을 해주어 같은 시간에 돌아갈 수 있는 방법을 구현했습니다.
[0, 0, 0, 0, 0, 0, 0, ... , 0] 예를 들어 빈 배열이 있을 때
[0, 1, 1, 1, 0, 0, 0, 1, 1, 0] 이런 상황에는 두 학생이 동시에 돌아갈 수 있게 되는 것입니다.
이런 방법을 반복하여 모든 학생들이 지나치는 복도의 인덱스를 +1 씩 해주어
리스트에서 가장 높은 값이 모든 학생들이 돌아가기 위해 걸리는 시간이 된다고 생각하고 문제를 풀었습니다.
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    return_arr = [list(map(int, input().split())) for _ in range(N)]    # 출발하고 돌아가야 할 학생의 방 번호
    room_arr = [0] * 200    # 빈 복도의 배열
    return_cnt = 1  # 최소 시간

    for arr in return_arr:  # 출발하는 방 번호를 더 적은 번호로 놓기 위하여 정렬
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

    student_arr = [0] * N

    for i in range(N):
        start = return_arr[i][0]  # 출발하는 방 번호
        end = return_arr[i][1]    # 도착하는 방 번호
        student = list(range(start // 2 + start % 2 - 1, end // 2 + end % 2))  # 방 번호가 짝수, 홀수인 경우를 고려하여
        student_arr[i] = student    # i번째 학생이 거치는 복도의 인덱스를 리스트에 저장
        for num in student_arr[i]:  # i번째 학생이 거치는 복도의 인덱스를
            room_arr[num] += 1  # 비어있는 복도의 인덱스에 하나씩 더해준다

    for j in range(199):    # 학생들이 가장 많이 지나친 복도의 횟수를 구하기 위한 반복문
        if room_arr[j] >= room_arr[j + 1]:
            room_arr[j], room_arr[j + 1] = room_arr[j + 1], room_arr[j]

    print(f'#{test_case + 1} {room_arr[-1]}')

