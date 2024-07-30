T = int(input())

for test_case in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    answer = num_list[-1] - num_list[0]
    print(f'#{test_case+1} {answer}')
