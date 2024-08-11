import sys
sys.stdin = open('input.txt', 'r')

T = int(input())                    # 테스트 케이스


def split_num(num):                 # 양의 번호를 각 자릿수로 나눈 후 리스트에 저장하는 함수
    num_list = []
    while num > 0:                  # 몫이 0이 될 때까지 반복
        num_list.append(num % 10)
        num //= 10
    return num_list


for test_case in range(T):
    N = int(input())
    num_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}  # 모든 숫자가 채워지는지 확인하기 위한 딕셔너리
    times = 1
    while True:
        num_list = split_num(N * times)  # 함수를 호출하여 N*times가 각 자릿수로 나눠진 리스트를 받아온다
        for num in num_list:            # 리스트의 숫자에 해당하는 key에 value를 1씩 추가
            num_dict[num] += 1
        for v in num_dict.values():     # 딕셔너리 value에 0이 나오면 다음 반복으로
            if v == 0:
                break
        else:                           # 딕셔너리 value가 모두 0보다 크면
            break                       # while 종료
        times += 1
    print(f'#{test_case+1} {N * times}')
