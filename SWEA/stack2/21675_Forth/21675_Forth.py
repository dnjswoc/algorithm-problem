import sys
sys.stdin = open('input.txt')

T = int(input())                        # 테스트 케이스 입력


def forth(ep):                          # forth 함수 정의
    stack = []                          # 빈 스택 생성
    for factor in ep:                   # 입력 값 순회
        if factor.isdigit():            # 숫자이면
            stack += [factor]           # 스택에 저장
        elif factor in arithmetic:      # 사칙연산이면
            if len(stack) < 2:          # 스택의 길이가 2보다 작으면
                return 'error'          # 연산 불가함으로 error return
            num_2 = int(stack.pop())    # 처음 pop 한 값을 num_2
            num_1 = int(stack.pop())    # 다음 pop 한 값을 num_1
            if factor == arithmetic[0]:  # 사칙 연산으로 계산하여
                result = num_1 + num_2
            elif factor == arithmetic[1]:
                result = num_1 - num_2
            elif factor == arithmetic[2]:
                result = num_1 * num_2
            else:
                result = num_1 // num_2
            stack += [result]           # 계산 결과를 스택에 저장
        if factor == '.':               # 순회하며 .을 만나면
            if len(stack) == 1:         # 스택의 길이가 1이면 연산 완료로
                return stack.pop()      # pop한 값을 return
            else:                       # 스택의 길이가 1이 아니면 연산 완료하지 못하였으므로
                return 'error'          # error return


for test_case in range(T):              # 테스트 케이스만큼 반복
    expression = list(input().split())  # 문자열 입력
    arithmetic = ['+', '-', '*', '/']   # 사칙 연산 리스트 생성
    answer = forth(expression)          # forth 함수 호출
    print(f'#{test_case+1} {answer}')   # output 출력
