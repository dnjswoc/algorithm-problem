import sys
sys.stdin = open('input.txt', 'r')

T = int(input())                # 테스트 케이스

for test_case in range(T):
    ball_str = input()          # 문자열 입력
    ball_type = ['(', ')']      # 공의 형태
    ball_count = 0              # 공의 개수
    for i in range(len(ball_str)):
        if ball_str[i] in ball_type:    # 공의 형태 중 하나만 있어도
            ball_count += 1             # count 1씩 증가
    for j in range(len(ball_str) - 1):
        if ball_str[j] == '(' and ball_str[j + 1] == ')':   # 온전한 공이 있으면
            ball_count -= 1             # count 1씩 감소
    print(f'#{test_case+1} {ball_count}')
