T = int(input())                            # 테스트 케이스 입력


def cal_change(price, change_dict):         # 잔돈 계산하는 함수
    for changes in change_dict.keys():      # 딕셔너리의 key를 반복하여
        quotient = price//int(changes)      # key값을 정수형으로 바꿔 몫을 계산하고
        change_dict[changes] += quotient    # 딕셔너리 value에 몫을 더하고
        price %= int(changes)               # 나머지를 다음 반복에 넘겨준다.
    return change_dict                      # 반복이 끝난 딕셔너리를 return


for test_case in range(T):                  # 테스트 케이스만큼 반복
    N = int(input())                        # 잔돈 입력
    change = {'50000': 0, '10000': 0, '5000': 0, '1000': 0, '500': 0, '100': 0, '50': 0, '10': 0}   # 잔돈 딕셔너리 초기화
    coins = cal_change(N, change)           # 잔돈 계산하는 함수 호출
    print(f'#{test_case+1}')                # output 출력
    for coin in coins:
        print(coins[coin], end=' ')
    print()
