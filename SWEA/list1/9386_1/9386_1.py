# import sys
# sys.stdin = open('input.txt')

T = int(input())                        # 테스트 케이스 입력

for test_case in range(T):              # 테스트 케이스만큼 반복
    N = int(input())                    # 입력될 숫자 개수
    num_line = input()                  # 숫자 입력(str로 받음)
    num_list = []                       # 입력된 숫자열에 1이 있는 인덱스를 리스트에 저장
    num_count = 0                       # num_list의 길이 측정
    for num in range(N):                # N만큼 반복
        if int(num_line[num]) == 1:     # 입력된 숫자열에 1이 있으면
            num_list += [num]           # 그 인덱스를 리스트에 저장
            num_count += 1
    num_seq_count = 1                   # 1이 연속된 값 측정(1이 초깃값)
    num_seq_list = []                   # 연속된 값이 저장될 리스트 생성
    for i in range(num_count-1):        # 리스트 크기-1 만큼 반복
        if num_list[i] == num_list[i+1] - 1:    # 다음 반복과 비교하여 인덱스가 1이 차이나면
            num_seq_count += 1          # 카운트에 1 추가
        else:
            num_seq_list += [num_seq_count]  # 그렇지 않으면 이때까지의 값을 리스트에 저장하고 
            num_seq_count = 1           # 연속된 값 1로 초기화
        if i == num_count-2:            # 마지막 반복에 도착하면
            num_seq_list += [num_seq_count]  # 마지막 반복까지의 연속된 값을 리스트에 저장
    max_seq_count = num_seq_list[0]     # 리스트에서 1이 연속된 횟수의 최댓값 구하기
    for i in range(len(num_seq_list)-1):
        if max_seq_count < num_seq_list[i+1]:
            max_seq_count = num_seq_list[i+1]
    print(f'#{test_case+1} {max_seq_count}')    # output 출력
