T = int(input())

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_count=0
    for j in range(N):
        if num_list[j] > 0:
            num_count+=1
        print(num_count)
    print(num_list)
    # print(f'#{i+1} {answer}')