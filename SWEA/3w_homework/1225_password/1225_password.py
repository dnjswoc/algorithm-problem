import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    T = int(input())
    data_list = list(map(int, input().split()))
    while True:
        for i in range(1, 6):
            data_list.append(data_list.pop(0) - i)  # 첫 번째 숫자를 1 ~ 5만큼 빼는 cycle
            if data_list[-1] <= 0:          # 숫자가 감소할 때 0보다 작아지면
                data_list[-1] = 0           # 0으로 저장하면 반복문 종료
                break
        if data_list[-1] == 0:
            break
    print(f'#{T}', end=' ')
    for num in data_list:
        print(num, end=' ')
    print()
