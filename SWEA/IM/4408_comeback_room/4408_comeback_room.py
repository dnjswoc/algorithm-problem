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

