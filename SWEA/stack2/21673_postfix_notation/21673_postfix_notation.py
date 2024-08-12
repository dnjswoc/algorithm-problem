import sys
sys.stdin =open('input.txt')

T = int(input())                            # 테스트 케이스 입력


def change_notation(ep):                    # 후위표기법으로 변경하는 함수
    stack = []                              # 스택 생성
    result = []                             # 결과값 저장할 리스트 생성
    for char in ep:                         # 입력값 순회
        if char in num:                     # char이 피연산자이면
            result += [char]                # result 리스트에 저장
            continue
        if char in arithmetic.keys():     # char이 연산자이면(소괄호 포함)
            if stack:                       # 스택에 연산자가 있으면
                if char == '(':             # char이 소괄호라면
                    stack += [char]         # 스택에 저장
                    continue                # 다음 반복으로
                while arithmetic[stack[-1]] >= arithmetic[char]:    # 연산자의 우선순위가 스택의 마지막 연산자보다 작을 때까지 반복
                    a = stack.pop()         # 스택에서 pop
                    result += [a]           # pop한 값을 result 리스트에 저장
                    if not stack:           # 빈 리스트가 되면
                        break               # break
            stack += [char]                 # 스택에 연산자가 없거나 연산자 우선순위가 스택의 마지막 연산자보다 크면 스택에 연산자 저장
            continue
        if char == ')':                   # char이 닫는 괄호라면
            while stack[-1] != '(':         # 열린 괄호가 나올 때까지 반복
                tmp = stack.pop()             # 스택에서 pop하여
                result += [a]               # result에 저장
            stack.pop()                     # 스택에 남은 열린 괄호 제거
    else:                                   # 위 for문 반복이 끝난 후
        # if stack:                           # 스택에 연산자가 남아있으면
        while stack:                    # 빈 스택이 될 때까지
            a = stack.pop()             # 스택 pop
            result += [a]               # result에 연산자 저장

    return result                           # result return


for test_case in range(T):                  # 테스트 케이스만큼 반복
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']    # 문자열에서 숫자열로 인식하기 위한 리스트 생성
    arithmetic = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}       # 연산자 우선순위 지정
    expression = input()                    # 문자열 입력
    new_expression = change_notation(expression)    # 후위표기법으로 변경
    print(f'#{test_case+1}', end=' ')       # output 출력
    for answer in new_expression:
        print(answer, end='')
    print()
