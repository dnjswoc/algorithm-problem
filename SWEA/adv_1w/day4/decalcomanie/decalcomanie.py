import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    word_arr = list(input())
    max_cnt = 0  # 가장 긴 데칼코마니를 구할 변수

    for i in range(N):
        dec_cnt = 1  # 시작할 때의 데칼코마니 길이
        j = 1   # 좌우로 늘어날 인덱스의 수
        while i - j >= 0 and i + j < N:  # 인덱스를 벗어날 때까지
            if word_arr[i - j] == word_arr[i + j]:  # 같은 간격이 멀어질 때의 값이 같으면
                dec_cnt += 2    # 데칼코마니 길이는 +2
                j += 1  # 인덱스는 +1
                continue
            if word_arr[i - j] != word_arr[i + j]:
                break
        if max_cnt <= dec_cnt:
            max_cnt = dec_cnt

    print(f'#{test_case} {max_cnt}')
