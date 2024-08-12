# import sys
# sys.stdin = open('input.txt')

T = int(input())                            # 테스트 케이스 입력


def check_bracket(bracket):                 # 스택으로 괄호의 짝이 맞는지 확인
    stack = []
    bracket_dict = {'(': ')', '{': '}', '[': ']'}
    for char in bracket:                    # 문자열 순회
        if char in bracket_dict.keys():     # 순회하는 문자가 열린 괄호에 해당하면
            stack += [char]                 # stack 리스트에 저장
        elif char in bracket_dict.values():  # 순회하는 문자가 닫힌 괄호에 해당하면
            if not stack or char != bracket_dict[stack[-1]]:    # 빈 리스트이거나 문자가 리스트 마지막 괄호와 짝이 아니면
                return False                # False return
            stack.pop()                     # 아니면 pop
    return not stack                        # 빈 리스트이면 True return


for test_case in range(T):                  # 테스트 케이스만큼 반복
    bracket = input()                       # 문자열 입력
    if check_bracket(bracket):              # return value가 True이면
        print(f'#{test_case+1} 1')          # 1 출력
    else:                                   # 아니면
        print(f'#{test_case+1} -1')         # -1 출력
