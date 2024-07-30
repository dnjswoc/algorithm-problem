T = int(input())

num_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
num_list = [2, 3, 5, 7, 11]
num_zip = list(zip(num_dict, num_list))

for i in range(1, T+1):
    N = int(input())
    for j in num_zip:
        while N % j[1] == 0:
            N //= j[1]
            num_dict[j[0]] += 1
    print(f'#{i} {num_dict["a"]} {num_dict["b"]} {num_dict["c"]} {num_dict["d"]} {num_dict["e"]}')
    num_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
