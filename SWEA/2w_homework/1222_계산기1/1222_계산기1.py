import sys
sys.stdin = open('input.txt')


def postfix(exp):                       # 후위표기법으로 바꾸는 함수 정의
    stack = []                          # 스택 생성
    result = []                         # 결과를 나타낼 리스트 생성
    for ep in exp:                      # 입력 문자열 순회
        if ep.isdigit():                # 순회하는 문자가 숫자면
            result.append(ep)           # result 리스트에 저장
            continue                    # 다음 반복으로
        if ep == '+':                   # 순회하는 문자가 +라면
            if not stack:               # 스택이 비어있다면
                stack.append(ep)        # 스택에 + 저장
                continue                # 다음 반복으로
            result.append(stack.pop())  # 스택이 비어있지 않다면 스택에서 pop하여 result 리스트에 저장
            stack.append(ep)            # 그리고 +를 스택에 저장
    else:                               # 반복이 끝나면
        result.append(stack.pop())      # 스택에 남은 마지막 +을 pop하여 result 리스트에 저장
    return result                       # result return


def calculator(exp):                    # 후위표기법을 계산하는 함수 정의
    stack = []                          # 스택 생성
    for ep in exp:                      # 입력 받은 문자열 순회
        if ep.isdigit():                # 순회하는 문자가 숫자면
            stack.append(ep)            # 스택에 저장
            continue                    # 다음 반복으로
        if ep == '+':                   # 순회하는 문자가 +라면
            v2, v1 = int(stack.pop()), int(stack.pop())  # 스택에 저장되어 있는 숫자 두 개를 pop
            stack.append(v1 + v2)       # 그 두 숫자를 더하여 스택에 다시 저장
    else:                               # 반복이 끝나 계산을 다 마치면
        return stack.pop()              # 마지막으로 계산된 숫자를 pop하여 return


for test_case in range(10):             # 테스트 케이스 10개 반복
    N = int(input())                    # 문자열 길이 입력
    expr = input()                      # 문자열 입력
    new_expr = postfix(expr)            # 입력 받은 문자열을 후위표기법으로 변환
    answer = calculator(new_expr)       # 변환된 후위표기법의 상태로 계산 실행 
    print(f'#{test_case+1} {answer}')   # output 출력
