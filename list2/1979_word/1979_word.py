T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    word_arr = [list(map(int, input().split())) for _ in range(N)]
    for row in range(N):
        list_1 = []
        count = 0
        for col in range(N):
            if word_arr[row][col] > 0:
                count += 1
            elif word_arr[row][col] == 0:
                list_1 += [count]
                count = 0
        print(list_1)
