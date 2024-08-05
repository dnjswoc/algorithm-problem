def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M + 1)
    # preprocessing
    j = 0   # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j          # p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # search
    i = 0   # 비교할 텍스트 위치
    j = 0   # 비교할 패턴 위치
    while i < N and j<= M:
        if j == -1 or t[i] == p[j]:     # 첫 글자가 불일치했거나, 일치하면
            i += 1
            j += 1
        else:                           # 불일치
            j = lps[j]
        if j == M:                      # 패턴을 찾을 경우
            print(i - M, end=' ')       # 패턴의 인덱스 출력
            j = lps[j]
    print()
    return


t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)

