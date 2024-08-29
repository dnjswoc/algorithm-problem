import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}   # 16진수의 10이상의 경우

for test_case in range(T):
    N, H = input().split()  # N: 16진수 자릿수, H : 16진수
    total = []

    for num in H:
        binary = []
        if num in hex_dict.keys():  # 딕셔너리 키에 해당하면
            num = hex_dict[num]  # 10진수 숫자로 바꿈
        elif num.isdecimal():   # 9이하의 수가 나오면
            num = int(num)  # 10진수 숫자로 바꿈
        while num >= 1:  # num이 1보다 클 때까지 반복
            binary.append(str(num % 2)) # 2로 나눈 나머지를 문자열로 변환 후 리스트에 저장
            num //= 2   # num을 2로 나눈 몫으로 재할당
        while len(binary) < 4:  # 4자리가 될 때까지 0추가
            binary.append('0')
        total.extend(binary[::-1])  # 뒤집어서 total에 저장
    print(f"#{test_case + 1} {''.join(total)}")
