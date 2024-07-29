T = int(input())

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    count=0
    num_count=0
    for num in num_list:
        count+=1
    for j in range(count):
        if num_list[j] > 0:
            num_count+=1
    print(num_list)
    # print(f'#{i+1} {answer}')