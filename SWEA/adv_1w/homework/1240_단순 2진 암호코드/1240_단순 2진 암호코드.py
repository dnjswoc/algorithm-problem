import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

password_dict = {'0001101': 0,
                 '0011001': 1,
                 '0010011': 2,
                 '0111101': 3,
                 '0100011': 4,
                 '0110001': 5,
                 '0101111': 6,
                 '0111011': 7,
                 '0110111': 8,
                 '0001011': 9}


def find_password(arr):
    for i in range(N):
        for j in range(M - 1, -1, -1):  # 오른쪽 위에서부터 시작해 1이 가장 먼저 나오는 인덱스 추출
            if arr[i][j]:
                return i, j


def check_password(arr):
    pw = []
    for lst in arr:     # 리스트를 하나씩 반복하며 하나의 문자열로 변환
        pws = ''
        for j in range(len(lst)):
            pws += str(lst[j])
        if pws in password_dict.keys():  # 변환한 문자열이 암호 코드에 해당하면
            pw.append(password_dict[pws])   # 해독한 암호를 pw 리스트에 저장

    sum_pw = 0  # 해독한 암호가 올바른지 알아보기 위한 변수
    for i in range(8):
        if i % 2 == 0:  # 홀수 자리의 합 * 3
            sum_pw += (pw[i] * 3)
        else:
            sum_pw += pw[i]
    if sum_pw % 10 == 0:    # 조건에 맞춰 더한 값이 10의 배수이면
        return sum(pw)  # 해독한 암호의 답을 더해준 뒤 return
    else:
        return 0    # 그렇지 않으면 0 return


for test_case in range(T):
    N, M = map(int, input().split())
    num_arr = [list(map(int, input())) for _ in range(N)]
    x, y = find_password(num_arr)   # 우상단에서 시작해 1이 가장 먼저 나오는 인덱스
    password_arr = num_arr[x][y-55:y+1]  # 암호 56개
    split_arr = [0] * 8  # 7자리씩의 암호 8개를 나누어 담을 리스트

    for i in range(1, 9):
        split_arr[i - 1] = password_arr[7 * (i - 1):7 * i]

    print(f'#{test_case+1} {check_password(split_arr)}')
