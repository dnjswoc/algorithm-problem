import sys
sys.stdin = open('input.txt')

T = int(input())                        # 테스트 케이스 입력

for test_case in range(T):              # 테스트 케이스만큼 반복
    N = int(input())                    # 숫자 카드 개수 입력
    num_line = input()                  # 숫자 카드 입력
    num_list = []                       # 숫자 카드를 정수형 리스트로 변환
    for num in num_line:
        num_list += [int(num)]
    for i in range(N-1):                # 최댓값을 찾기 위해 정렬
        if num_list[i] > num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
    max_num = num_list[-1]              # 숫자 카드의 최댓값
    counts = [0] * (max_num + 1)        # 숫자 카드 카운트를 위해 최댓값 +1 만큼 0리스트를 생성
    for num in num_list:                # 숫자 카드의 개수를 세기 위해 반복
        counts[num] += 1
    frequent_times = counts[0]          # 최빈값을 0으로 설정
    for num in range(max_num):          # 최댓값 만큼 반복하여 최빈값을 구한다.
        if frequent_times < counts[num+1]:
            frequent_times = counts[num+1]
    frequent_num = 0                    # 최빈값에 해당하는 숫자 카드 구한다.
    for num in range(max_num, -1, -1):
        if counts[num] == frequent_times:
            frequent_num = num
            break
    print(f'#{test_case+1} {frequent_num} {frequent_times}')    # output 출력
