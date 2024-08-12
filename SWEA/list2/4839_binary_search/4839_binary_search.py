import sys
sys.stdin = open("input.txt", "r")


def page_times(pages, target_page):
    count = 1
    start = 1
    high = pages
    mid = (start + high)//2
    while mid != target_page:
        if mid > target_page:
            high = mid
        elif mid < target_page:
            start = mid
        mid = (start + high)//2
        count += 1
    return count


T = int(input())

for test_case in range(T):
    P, A, B = map(int, input().split())
    P_A = page_times(P, A)
    P_B = page_times(P, B)
    if (1 <= P <= 1000) and (1 <= P_A <= 1000) and (1 <= P_B <= 1000):
        if P_A < P_B:
            answer = 'A'
        elif P_A == P_B:
            answer = 0
        else:
            answer = 'B'
        print(f'#{test_case+1} {answer}')
