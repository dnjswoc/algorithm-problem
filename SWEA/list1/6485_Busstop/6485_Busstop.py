import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def to_range():     # 버스 노선이 다니는 정류장을 리스트로 표현
    new_arr = []
    for stop in end_stop:
        new_arr.append(list(range(stop[0], stop[1] + 1)))
    return new_arr


def check_busstop():    # 해당 버스 정류장에 다니는 노선의 수를 계산
    pass_by_count = [0] * P
    for num in range(P):    # 해당 버스 정류장과 노선마다 비교하여 노선에 들어가면 count += 1
        for end in end_stop:
            if bus_stop_list[num] in end:
                pass_by_count[num] += 1
    return pass_by_count


for test_case in range(T):
    N = int(input())
    end_stop = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stop_list = []
    for i in range(P):
        bus_stop_list.append(int(input()))
    end_stop = to_range()
    print(f'#{test_case+1}', end=' ')
    print(*check_busstop())

