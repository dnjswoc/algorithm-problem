import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = float(input())  # 실수형으로 받기
    binary = []  # 이진수로 변환하기 위한 리스트
    i = 1
    while N > 0:
        if N >= 2 ** (-i):  # N이 2의 -i제곱 보다 크면 2의 -i제곱이 +1 되고
            N -= 2 ** (-i)
            binary.append('1')  # 리스트에 1을 저장
        else:
            binary.append('0')  # N이 2의 -i제곱 보다 작으면 뺄 수 없으므로 2의 -i제곱은 0이 된다.
        i += 1
        if len(binary) >= 13:   # 리스트 길이가 13이 넘어가면 overflow
            break
    if len(binary) >= 13:
        print(f'#{test_case + 1} overflow')
    else:
        print(f"#{test_case + 1} {''.join(binary)}")