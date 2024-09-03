import sys
sys.stdin = open('input.txt', 'r')


T = int(input())


def bubble_sort(arr):   # 도착 시간 기준으로 오름차순 정렬
    for i in range(N - 1, -1, -1):
        for j in range(i):
            if arr[j][1] >= arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


for test_case in range(1, T + 1):
    N = int(input())
    time_arr = [list(map(int, input().split())) for _ in range(N)]
    bubble_sort(time_arr)

    s, e, cnt = 0, 0, 0  # s : 작업 시작 시간, e : 작업 완료 시간, cnt : 화물차 이용 횟수
    for arr in time_arr:
        if arr[0] < e:  # 다음 화물차의 작업 시작 시간이 도크 작업 완료시간보다 빠르면
            continue
        # 도크 작업 완료시간보다 다음 화물차 작업 시작 시간이 느리고
        # 도크 작업 완료시간이 화물차 작업 완료 시간보다 빠르면 ex. 14시에 끝나는데 다음 화물차 작업 완료 시간이 18시면
        if e <= arr[1]:
            e = arr[1]   # arr[1]을 작업 완료 시간으로 설정
            s = arr[0]   # arr[0]을 작업 시작 시간으로 설정
            cnt += 1
            continue

    print(f'#{test_case} {cnt}')



# 나영이 풀이
T = int(input())

for case in range(1, T+1):
    N = int(input())  # 신청서 N
    dohc = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):    # 시작시각 종료시각 앞뒤로 바꿔줌
        dohc[i][0], dohc[i][1] = dohc[i][1], dohc[i][0]

    dohc.sort()   # 도착시간 기준으로 오름차순 정렬   [[14, 4], [18, 8], [20, 17], [23, 20], [24, 23]]

    cnt = 0   # 작업 카운트
    now = 0  # 0시부터 작업 시작

    for i in range(N):
        start = dohc[i][1]  # 시작 시각
        end = dohc[i][0]  # 종료 시각

        if now <= start:
            cnt +=1
            now = end

    print(f'#{case} {cnt}')

