T = int(input())                    # 테스트 케이스 입력

for test_case in range(T):          # 테스트 케이스만큼 반복
    N = int(input())                # N : 가로의 길이
    num_list = list(map(int, input().split()))  # 쌓여있는 상자의 수
    max_list = num_list[:]          # 쌓여있는 상자 수의 최댓값을 구할 리스트 생성
    minus_list = num_list[:]        # 낙차를 구할 리스트 생성
    for j in range(N-1):            #
        if max_list[j] > max_list[j+1]:
            max_list[j], max_list[j+1] = max_list[j+1], max_list[j]
    max_num = max_list[-1]
    stack_list = [0] * max_num
    if max_num == 0:
        print(f'#{test_case+1} 0')
        continue
    for i in range(max_num):
        num_count = 0
        for k in range(N):
            if minus_list[k] > 0:
                num_count += 1
            minus_list[k] -= 1
        stack_list[i] = num_count
    max_fall_list = [0] * max_num
    for p in range(N):
        fall_list = [0] * max_num
        for q in range(max_num):
            if q > num_list[p] - 1:
                continue
            fall_list[q] = (N - p) - stack_list[q]
            if fall_list[q] <= 0:
                fall_list[q] = 0
        for q in range(max_num-1):
            if fall_list[q] > fall_list[q+1]:
                fall_list[q], fall_list[q+1] = fall_list[q+1], fall_list[q]
        if p < max_num:
            max_fall_list[p] = fall_list[-1]
    for r in range(max_num - 1):
        if max_fall_list[r] > max_fall_list[r+1]:
            max_fall_list[r], max_fall_list[r+1] = max_fall_list[r+1], max_fall_list[r]
    answer = max_fall_list[-1]
    print(f'#{test_case+1} {answer}')