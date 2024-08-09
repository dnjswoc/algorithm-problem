import sys
sys.stdin = open('input.txt', 'r')

T = int(input())            # 테스트 케이스

for test_case in range(T):
    N, K = map(int, input().split())    # N : 수강생 수, K : 과제를 제출한 사람 수
    submit_arr = list(map(int, input().split()))    # 과제 제출 명단
    student_list = list(range(1, N+1))  # 수강생 명단
    print(f'#{test_case+1}', end=' ')
    for num in student_list:            # 수강생 번호가 과제 제출 명단에 없으면
        if num not in submit_arr:
            print(num, end=' ')         # 출력
    print()
