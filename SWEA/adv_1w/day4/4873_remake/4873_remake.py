# import sys
# sys.stdin = open('input_1.txt', 'r')
# sys.stdout = open('output_1.txt', 'w')

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


# 나영
def remove_repeat_ch(password):
    score = 0
    stack = []
    cnt = 1
    for ch in password:
        if not stack or stack[-1][0] != ch:
            cnt = 1
            stack.append([ch, cnt])
        else:
            stack[-1][1] += cnt

    # [['X', 1], ['A', 2], ['Y', 1], ['B', 3], ['C', 1], ['D', 2], ['C', 1], ['Z', 1], ['D', 1]]

    word = ''
    for li in stack:
        if li[-1] >= 2:
            score += li[-1]
        else:
            word += li[0]

    return score, word  # (7, 'XYCCZD')


def continuous_password(password):  # 연속문자 탐색하는 악질함수
    cnt = 1
    total = 0

    res = list(map(lambda ch: ord(ch), password))  # ord 문자열을 숫자로 바꿔주는 내장함수

    for i in range(1, len(res)):
        if res[i] == res[i - 1] + 1:  # 연속인지 알아보기 위함
            cnt += 1
        else:
            if cnt > 1:
                total += cnt
                cnt = 1
    else:
        if cnt > 1:  # 하... 할말하않 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
            total += cnt

    return total


T = int(input())

for case in range(1, T + 1):
    password = input()  # XAAYBBBCDDCZD
    ans = 0

    while True:
        score, password = remove_repeat_ch(password)
        ans += score  # 전체 점수
        if score == 0:  # 점수가 0이란건 repeat되는게 없다는 뜻 반복문 탈출
            break

    print(f'#{case} {ans + continuous_password(password)}')
