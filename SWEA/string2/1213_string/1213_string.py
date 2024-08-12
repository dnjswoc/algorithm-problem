# import sys
# sys.stdin = open('input.txt', encoding='UTF-8')


def brute_force(p, t):              # brute-force 알고리즘으로 패턴 매칭
    i = 0                           # 패턴의 인덱스
    j = 0                           # 문자열의 인덱스
    count = 0                       # 문자열과 패턴이 일치하는 횟수
    while j < p_count and i < text_count:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == p_count:            # 패턴과 문자열이 일치하면
            count += 1              # count 1씩 증가
            i = i - j + 1           # 인덱스 리셋
            j = 0
    return count                    # count return


for t in range(10):                 # 10번 반복
    N = int(input())                # 케이스 넘버 입력
    pattern = input()               # 패턴 입력
    text = input()                  # 문자열 입력
    p_count = 0                     # 패턴 길이
    text_count = 0                  # 문자열 길이
    for num in pattern:
        p_count += 1
    for num in text:
        text_count += 1
    answer = brute_force(pattern, text)  # 패턴 매칭 함수 호출
    print(f'#{N} {answer}')         # output 출력
