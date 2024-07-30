T = int(input())

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_count = 0
    stack_list = []
    for j in range(N):
        after_list = [0] * 100
        for k in range(100):
            if num_list[j] > 0:
                num_count += 1
                num_list[j] - 1
            after_list[k] = num_count
        print(num_count)
        print(after_list)
    print(num_list)
    # print(f'#{i+1} {answer}')