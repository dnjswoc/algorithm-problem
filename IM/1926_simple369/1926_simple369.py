N = int(input())
num_arr = list(range(1, N+1))

for num in num_arr:
    if (num // 10 == 3) or (num // 10 == 6) or (num // 10 == 9):
        print(num)