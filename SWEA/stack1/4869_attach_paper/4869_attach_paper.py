# 22:10 - 23:10
import sys
sys.stdin = open('input.txt', 'r')


def factorial(n):   # 팩토리얼을 구하는 함수
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def paper(c_10, c_20):  # 가로의 길이가 10, 20인 종이의 수가 주어졌을 때 나올 수 있는 경우의 수를 구하는 함수
    # ex. 가로의 길이가 10인 종이의 개수가 3, 가로의 길이가 20인 종이의 개수가 2일 때
    # factorial(3 + 2) / (factorial(3) * factorial(2))를 하면 경우의 수가 나온다.
    # 그리고 가로의 길이가 20인 종이는 가로로 자를 수 있는 2가지의 경우가 있기 때문에
    # 가로의 길이가 20인 종이의 개수 만큼 2를 곱해준다.
    case = (factorial(c_10 + c_20)) / (factorial(c_10) * factorial(c_20))
    return int(case) * (2 ** c_20)


T = int(input())

for test_case in range(T):
    N = int(input())
    cnt_10 = N // 10
    cnt_20 = 0
    cases = []

    while cnt_10 >= 0:
        cases.append(paper(cnt_10, cnt_20))
        cnt_10 -= 2     # 가로의 길이가 20인 종이 개수가 1 늘어나면 가로의 길이가 10인 종이 개수는 2씩 줄어든다
        cnt_20 += 1

    print(f'#{test_case + 1} {sum(cases)}')
