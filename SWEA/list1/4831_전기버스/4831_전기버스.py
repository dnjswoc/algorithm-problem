# 12:30 - 13:56
import sys
sys.stdin = open('input.txt', 'r')

'''
전기버스가 종점까지 향하면서 충전기가 설치된 정류장에서 충전을 하고 K만큼 갈 때
그 거리보다 큰 정류장 번호 바로 아래에서 충전을 하면 되겠다고 생각했습니다.
ex) K : 3, N : 10, M : 5
0   1   2   3   4   5   6   7   8   9   10  : 종점까지 정류장 번호
    o       o       o       o       o       : 충전기가 설치된 정류장
            o       o       o               : 충전한 정류장
위 예시를 보면 0에서 시작하여 K만큼 더하면 3이 되고, 그 거리보다 큰 정류장 번호는 5가 되는 것입니다.
그리고 그 정류장 바로 아래 번호에서 충전을 시키고, 다시 3번 정류장에서부터 앞의 행동을 반복합니다.
그리하여 종점까지 도착하면 운행이 가능한 것입니다.
하지만 테스트 케이스 2번을 보면, 위와 같은 방법을 적용했을 때,
충전하게 되는 정류장 번호는 3번이 연속으로 나옵니다. 이 말은 정류장에서 충전 후 K만큼 갔을 때,
충전한 바로 다음 정류장으로 갈 수 없다는 말이 되므로 0을 출력해야 합니다.
'''

T = int(input())

for test_case in range(T):
    K, N, M = map(int, input().split())     # K : 한 번 충전으로 이동할 수 있는 정류장 수, N : 종점, M : 충전기 개수
    M_list = list(map(int, input().split()))    # 충전기가 설치된 정류장 번호
    charge_num = 0      # 버스를 충전하는 정류소 번호
    charge_cnt = 0      # 버스를 충전하는 횟수
    charge_stop = []    # 버스를 충전하는 정류소 번호를 리스트에 저장

    while charge_num + K < N:   # 종점에 도착하면 반복문 종료

        for i in range(M):      # 충전기가 설치된 정류장 번호와 비교합니다.
            if charge_num + K < M_list[i]:  # 버스 충전한 정류장에서 갈 수 있는(K) 만큼 갔을 때의 거리 바로 다음의
                charge_num = M_list[i - 1]  # 충전할 수 있는 정류장 바로 아래 정류장의 번호에서 충전을 합니다
                break   # charge_num = 3일 때, charge_num + K = 6이 되고, 그러면 7번 정류장 바로 전 정류장(5번)에서 충전!
        else:
            charge_num = M_list[-1]  # 모든 충전소를 비교해봐도 charge_num + K가 클 때는 마지막 충전 정류소에서 충전!
        charge_stop.append(charge_num)  # 리스트에 충전했던 정류소 번호를 저장
        charge_cnt += 1  # 충전 횟수 +1

        for num in range(len(charge_stop) - 1):  # 리스트에 충전 정류소를 입력하면서 리스트 안의 값들과 비교
            if charge_stop[num] == charge_stop[num + 1]:    # 같은 충전 정류소가 입력되어 있으면 다음 충전 정류소까지 갈 수 없다는 의미이므로
                charge_cnt = 0  # 충전 횟수를 0으로 만들고, for 문 종료
                break
        if charge_cnt == 0: # 충전 횟수가 0이 되면 while 문 종료
            break
    print(f'#{test_case + 1} {charge_cnt}')
