T = int(input())                        # 테스트 케이스 입력


def carrot_sequence(car_list, num):     # 연속적으로 커지는 당근의 개수를 계산하는 함수
    seq_count = 1                       # 최소 크기가 1이므로 초깃값 1로 설정
    seq_count_list = []                 # 연속적으로 커지는 당근의 개수를 저장할 빈 리스트 생성
    for i in range(num-1):              # 입력 받은 리스트의 개수-1 만큼 반복
        if car_list[i] < car_list[i+1]:    # 다음 인덱스에서 크기가 커지면 +1
            seq_count += 1
        elif car_list[i] >= car_list[i+1]:   # 그렇지 않으면 1로 reset
            seq_count = 1
        seq_count_list += [seq_count]   # 연속적으로 커지는 당근의 개수를 리스트에 저장
    max_seq_count = max_count(seq_count_list, num-1)    # 리스트에서 최댓값을 구할 함수 호출
    return max_seq_count                # 위에서 호출한 함수의 반환 값을 return


def max_count(seq_list, num):           # 연속적으로 커지는 당근의 개수를 저장한 리스트에서 최댓값을 구할 함수
    max_seq_count = seq_list[0]         # 리스트의 0번째 인덱스를 초깃값으로 설정
    for i in range(num-1):              # 리스트의 개수-1만큼 반복
        if max_seq_count < seq_list[i+1]:   # 다음 인덱스 값이 커지면
            max_seq_count = seq_list[i+1]   # 다음 인덱스 값을 최댓값으로 재설정
    return max_seq_count                # 최댓값을 return


for test_case in range(T):              # 테스트 케이스만큼 반복
    N = int(input())                    # 당근 개수 입력
    carrot_list = list(map(int, input().split()))   # 당근 크기를 리스트로 입력
    seq_car_count = carrot_sequence(carrot_list, N)  # 연속적으로 커지는 당근의 개수를 구한다.
    print(f'#{test_case+1} {seq_car_count}')    # output 출력
