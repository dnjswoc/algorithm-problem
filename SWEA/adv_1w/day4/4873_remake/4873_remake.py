# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    str_lst = list(input())
    stack = []
    v = ''  # 마지막으로 stack에서 pop한 값을 저장하기 위한 변수

    for factor in str_lst:
        if factor == v:  # stack에서 마지막으로 pop한 값과 다음에 올 값이 같다면
            continue    # stack에 넣지 않기
        if not stack:   # stack이 비었으면 append
            stack.append(factor)
            v = ''      # 새로 stack에 append 했으므로 v reset
            continue
        if factor == stack[-1]:  # stack에 넣으려는 값이 stack의 마지막 값과 같다면
            v = stack.pop()     # stack에서 pop하고 그 값을 v에 저장
            continue
        stack.append(factor)    # stack이 비어있지 않고, 마지막 값과 같지 않으며, stack에서 마지막으로 pop한 값과도 다르면 append
        v = ''  # 새로 append 하였으므로 v reset
    answer = len(str_lst) - len(stack)  # 원래 문자열 길이에서 stack 길이를 빼주면

    cnt = 1  # 연속적으로 이어지는 문자열의 개수를 세기 위한 변수 ex) ABC = 3
    if len(stack) >= 2:  # stack의 길이가 2이상인 경우(2이상이어야 연속적일 수 없기 때문에)
        for i in range(1, len(stack)):  # 1번 인덱스부터 앞의 값과 비교
            if ord(stack[i - 1]) == ord(stack[i]) - 1:  # ASCII 번호가 1 늘어나면(연속적이면) cnt +1
                cnt += 1
            else:
                if cnt >= 2:    # 연속된 값이 있으면 cnt는 2 이상이고, 다음 값이 연속적이지 않으면
                    answer += cnt   # answer에 추가
                cnt = 1  # cnt reset
        else:   # 반복문이 다 끝나고
            if cnt >= 2:    # 연속적인 채로 끝나면
                answer += cnt   # answer에 추가
    print(f'#{test_case} {answer}')
