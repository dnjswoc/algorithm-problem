import sys
sys.stdin = open('input.txt', 'r')

arithmetic = {'+': 1, '*': 2}       # 연산자 딕셔너리 생성


def postfix(expr):                  # 후위표기법 변환 함수
    stack = []
    result = []
    for ep in expr:                 # 문자열 순회
        if ep.isdigit():            # 숫자면
            result.append(ep)       # result 리스트에 저장
            continue
        if ep in arithmetic:        # 연산자라면
            if not stack or arithmetic[ep] > arithmetic[stack[-1]]:  # 빈 stack이거나 우선순위가 높으면
                stack.append(ep)    # stack에 저장
                continue
            while arithmetic[ep] <= arithmetic[stack[-1]]:  # 빈 stack이 아니고 우선순위가 낮으면
                result.append(stack.pop())  # 우선순위가 높아질 때까지 stack pop
                if not stack:       # 빈 stack이 되면
                    break           # break
            stack.append(ep)        # while 문 종료 후 stack push
    else:
        while stack:                # 빈 스택이 될 때까지
            result.append(stack.pop())  # result에 저장
    return result


def calculator(expr):               # 계산하는 함수
    stack = []
    for ep in expr:                 # 문자열 순회
        if ep.isdigit():            # 숫자면
            stack.append(ep)        # stack push
            continue
        if ep in arithmetic:        # 연산자면
            v2, v1 = int(stack.pop()), int(stack.pop())  # 숫자 2개 pop
            if ep == '+':           # 연산자가 + 면 더한 후 stack push
                stack.append(v1 + v2)
            else:                   # 연산자가 * 면 곱한 후 stack push
                stack.append(v1 * v2)
    else:
        return stack.pop()          # 마지막 계산 값 return


for test_case in range(10):
    N = int(input())
    expr = input()
    pf_expr = postfix(expr)
    print(f'#{test_case+1} {calculator(pf_expr)}')
