# 16:25 - 17:15

'''
비밀번호를 만들기 위해 스택에 값을 하나씩 집어으면서
넣으려는 값이 스택의 마지막 값과 같다면 pop을 하는 방법을 써봤습니다.
'''

import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(10):
    N, P = input().split()
    pw_list = list(P)   # 입력받은 문자열을 리스트 형태로 변환
    stack = []  # 스택 생성
    for i in range(0, int(N)):  # 리스트 순회
        if not stack:   # 스택이 공백상태이면
            stack.append(pw_list[i])    # 스택에 저장
            continue
        if pw_list[i] == stack[-1]:  # 스택이 비어있지 않고, 스택에 넣으려는 값이 스택의 마지막 값과 같으면
            stack.pop()  # 스택의 마지막 값을 pop
            continue
        stack.append(pw_list[i])    # 스택이 비어있지 않고, 스택에 넣으려는 값과 마지막 값이 다르면 append
    print(f'#{test_case + 1}', end=' ')
    print(''.join(stack))
