import sys
sys.stdin = open('input.txt')

T = int(input())                            # 테스트 케이스 입력


def bracket_check(input_str):               # 괄호의 짝이 맞는지 확인하는 함수 정의
    stack = []                              # 스택 생성
    bracket_dict = {')': '(', '}': '{', ']': '['}   # 괄호의 짝을 검사하기 위한 딕셔너리 생성
    for char in input_str:                  # 문자열 순회
        if char in bracket_dict.values():   # 열린 괄호가 나오면
            stack += [char]                 # 스택에 저장
        elif char in bracket_dict.keys():   # 닫힌 괄호가 나오면
            if not stack or stack[-1] != bracket_dict[char]:    # 빈 스택이거나 스택의 마지막 값이 괄호의 짝이 맞지 않으면
                return False                # False return
            stack.pop()                     # 괄호의 짝이 맞으면 pop
    return not stack                        # 반복 후 빈 스택이 나오면 True return


for test_case in range(T):                  # 테스트 케이스만큼 반복
    input_code = input()                    # 문자열 입력
    if bracket_check(input_code):           # 함수 return value가 True이면
        print(f'#{test_case+1} 1')          # 1출력
    else:                                   # return value가 False이면
        print(f'#{test_case+1} 0')          # 0출력
