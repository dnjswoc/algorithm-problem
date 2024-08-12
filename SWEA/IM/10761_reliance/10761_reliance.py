import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    num_arr = list(input().split())
    target_dict = {'B': [], 'O': []}
    task_sequence = []
    for i in range(int(num_arr[0])):
        if num_arr[2 * i + 1] in target_dict.keys():
            target_dict[num_arr[2 * i + 1]].append(int(num_arr[2 * (i + 1)]))
        task_sequence.append(num_arr[2 * i + 1])
    print(target_dict)
    print(task_sequence)

