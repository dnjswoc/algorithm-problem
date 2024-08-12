# import sys
# sys.stdin = open('input.txt')

T = int(input())                    # 테스트 케이스 입력


def remove_repeat(seq_str):         # 반복된 문자열 제거하는 함수
    stack = []                      # 스택 생성
    for string in seq_str:          # 문자열 순회
        if string not in stack:     # 스택에 문자열이 없으면
            stack += [string]       # 스택에 문자열 저장
        elif string in stack:       # 스택에 문자열이 있으면
            if string == stack[-1]:  # 문자열이 스택 마지막 문자열과 같으면
                stack.pop()         # 스택 리스트 pop
            else:                   # 문자열이 스택 마지막 문자열과 다르면
                stack += [string]   # 스택에 추가
    list_count = 0                       # 스택 리스트이 개수
    for factor in stack:            # 스택 순회
        list_count += 1                  # count 1씩 증가
    return list_count                    # count return


for test_case in range(T):          # 테스트 케이스 반복
    input_str = input()             # 문자열 입력
    not_repeat_count = remove_repeat(input_str)  # 반복된 문자열 제거하는 함수 호출
    print(f'#{test_case+1} {not_repeat_count}')  # output 출력
